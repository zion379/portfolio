# Deploying HAM Website to Hetzner VPS (alongside the Portfolio)

This document is the step-by-step guide for an agent to deploy the HAM website
onto the same Hetzner VPS that already runs the `zionjohnson.dev` portfolio.
Run every command from the Claude workspace unless noted otherwise.

---

## Server Details

| | |
|---|---|
| **Host** | Hetzner VPS |
| **IP** | 5.78.233.143 |
| **SSH user** | `root` |
| **SSH key** | `/root/.ssh/id_ed25519` (already in this workspace) |
| **OS** | Ubuntu |
| **Existing services** | Nginx (reverse proxy), Docker, Certbot, `portfolio-app` container on port 5000 |
| **Portfolio repo** | `/root/portfolio` |

The HAM site runs as two Docker containers on a shared `ham-network` bridge:
- `ham-website` — Flask/Gunicorn app on internal port 5001
- `ham-db` — Postgres 15, internal only

Nginx routes `ham.zionjohnson.dev` → port 5001. The portfolio config is never touched.

> **Note:** Hetzner does not have `docker compose` installed. All containers are managed
> with plain `docker run`. The `docker-compose.yml` in the repo is used on the home server only.

---

## Step 0 — DNS (do this first, before everything else)

In the DNS provider for `zionjohnson.dev`, add:

| Name | Type | Value |
|---|---|---|
| `ham` | A | `5.78.233.143` |

Set proxy to **DNS only** (grey cloud in Cloudflare) so Certbot can reach the server directly.

Verify before continuing:
```bash
curl -sI http://ham.zionjohnson.dev
```
Should return `200 OK`.

---

## Step 1 — Push code to Hetzner

```bash
rsync -avz \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.env' \
  -e "ssh -i /root/.ssh/id_ed25519 -o StrictHostKeyChecking=no" \
  /workspace/HAM-website/ root@5.78.233.143:/root/ham-website/
```

---

## Step 2 — Create the .env file on Hetzner

```bash
ssh root@5.78.233.143 "cat > /root/ham-website/.env << 'EOF'
SECRET_KEY=<generate-a-strong-random-string>
DB_PASSWORD=<choose-a-strong-db-password>
DATABASE_URI=postgresql://ham_user:<same-db-password>@db:5432/ham_db
CDN_BASE_URL=https://pub-6bd27672c3354cc3a77629401fdd604e.r2.dev
MAIL_USER_NAME=
MAIL_PASSWORD=
STRIPE_SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
EOF"
```

Generate a SECRET_KEY with:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

The `.env` is excluded from rsync and must be created manually on the server.
The existing `.env` is already in place — only recreate if rotating credentials.

---

## Step 3 — Create Docker network and start database

```bash
ssh root@5.78.233.143 "docker network create ham-network"

ssh root@5.78.233.143 "docker run -d \
  --name ham-db \
  --network ham-network \
  --network-alias db \
  --restart unless-stopped \
  -e POSTGRES_DB=ham_db \
  -e POSTGRES_USER=ham_user \
  -e 'POSTGRES_PASSWORD=<DB_PASSWORD>' \
  -v ham_db_data:/var/lib/postgresql/data \
  postgres:15"
```

Wait for Postgres to be ready:
```bash
ssh root@5.78.233.143 "until docker exec ham-db pg_isready -U ham_user -d ham_db 2>/dev/null; do sleep 2; done && echo 'DB ready'"
```

> The `--network-alias db` flag is required. It makes `db` resolvable inside the network,
> matching what the `DATABASE_URI` expects. Without it the app cannot reach Postgres.

---

## Step 4 — Build and start the web container

```bash
ssh root@5.78.233.143 "cd /root/ham-website && docker build -t ham-website ."

ssh root@5.78.233.143 "docker run -d \
  --name ham-website \
  --network ham-network \
  --restart unless-stopped \
  -p 5001:5000 \
  --env-file /root/ham-website/.env \
  -v /root/ham-website/static/tmp_data:/app/static/tmp_data \
  ham-website"
```

Verify startup:
```bash
ssh root@5.78.233.143 "docker logs ham-website --tail 20"
```

You should see gunicorn workers booting with no errors.

---

## Step 5 — Add Nginx config for ham.zionjohnson.dev

```bash
ssh root@5.78.233.143 "
cat > /etc/nginx/sites-available/ham.zionjohnson.dev << 'EOF'
server {
    listen 80;
    server_name ham.zionjohnson.dev;

    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_read_timeout 60s;
    }
}
EOF

ln -sf /etc/nginx/sites-available/ham.zionjohnson.dev /etc/nginx/sites-enabled/ham.zionjohnson.dev
nginx -t && systemctl reload nginx
"
```

Do NOT touch `/etc/nginx/sites-enabled/zionjohnson.dev` — the portfolio config stays as-is.

---

## Step 6 — Get SSL cert (Let's Encrypt)

```bash
ssh root@5.78.233.143 "certbot --nginx \
  -d ham.zionjohnson.dev \
  --non-interactive \
  --agree-tos \
  -m zspynet22@icloud.com"
```

Certbot will edit the Nginx config to add the SSL block and set up auto-renewal.

---

## Step 7 — Verify

```bash
# Both HAM containers running:
ssh root@5.78.233.143 "docker ps | grep ham"

# Portfolio still works:
curl -sI https://zionjohnson.dev | head -3

# HAM site live over HTTPS:
curl -sI https://ham.zionjohnson.dev | head -3

# HAM app logs:
ssh root@5.78.233.143 "docker logs ham-website --tail 30"
```

---

## Future deploys (code changes)

```bash
# 1. Rsync code
rsync -avz \
  --exclude='.git' --exclude='__pycache__' --exclude='*.pyc' --exclude='.env' \
  -e "ssh -i /root/.ssh/id_ed25519 -o StrictHostKeyChecking=no" \
  /workspace/HAM-website/ root@5.78.233.143:/root/ham-website/

# 2. Rebuild and restart web container only (ham-db keeps running, data is safe)
ssh root@5.78.233.143 "
  cd /root/ham-website && \
  docker build -t ham-website . && \
  docker stop ham-website && docker rm ham-website && \
  docker run -d \
    --name ham-website \
    --network ham-network \
    --restart unless-stopped \
    -p 5001:5000 \
    --env-file /root/ham-website/.env \
    -v /root/ham-website/static/tmp_data:/app/static/tmp_data \
    ham-website
"
```

---

## Architecture

```
Internet (HTTPS)
      │
      ▼
Nginx — Hetzner 5.78.233.143
      ├── zionjohnson.dev        →  portfolio-app container  (127.0.0.1:5000)
      └── ham.zionjohnson.dev   →  ham-website container    (127.0.0.1:5001)
                                            │  ham-network bridge
                                         ham-db container (alias: db)
                                       (internal only, port never exposed)
```

---

## Notes

- `ham-db` data persists in Docker named volume `ham_db_data`. Rebuilding `ham-website` never touches the database.
- The `.env` on Hetzner is never synced by rsync (excluded). Keep credentials safe.
- Certbot auto-renews both certs (portfolio + HAM) via the same systemd timer.
- SSL cert expires 2026-09-13 (same as portfolio cert — both auto-renew).
- The `docker-compose.yml` in the repo is home-server only (uses Caddy `management_default` network).
