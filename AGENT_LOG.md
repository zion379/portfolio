# Portfolio Project — Agent Reference Log

This document is a full technical reference for AI agents working on this project. It covers the codebase architecture, infrastructure, asset pipeline, and maintenance procedures.

---

## Owner

**Zion Johnson** — Self-taught programmer and electrical engineer. K12 STEM instructor teaching circuit building and microcontroller programming on behalf of a technical college focused on STEM higher education.

- Email: zspynet22@icloud.com
- GitHub: github.com/zion379/portfolio

---

## Live Site

| Environment | URL | Notes |
|---|---|---|
| Production | https://zionjohnson.dev | Hetzner VPS, public internet |
| Dev/Local | http://100.101.69.31:5000 | Home server, LAN only |

---

## Codebase Overview

**Language/Framework:** Python 3.11 + Flask  
**Repo:** `github.com/zion379/portfolio`  
**Active branch:** `portfolio-revival`  
**Workspace path (Claude):** `/workspace/Personal-Portfolio-Website`

### Key Files

| File | Purpose |
|---|---|
| `portfolio.py` | Flask app entry point — all routes, OpenAI integration, R2 URL injection |
| `modules/project.py` | Data models: `Project_obj`, `Content_group`, `Carousel_obj`, `proj_content_obj` |
| `modules/projects_content.py` | All project content definitions — edit this to add/change projects |
| `modules/item_tracker_app/item_tracker.py` | Item tracker module with count/goal/note system |
| `templates/base.html` | Global layout — navbar, glass styles, constellation canvas animation |
| `templates/index.html` | Hero landing page |
| `templates/projects.html` | Project card grid |
| `templates/project_view.html` | Individual project page renderer |
| `templates/skills.html` | Skills page with category grouping and emoji icons |
| `sync_to_r2.py` | Syncs local/NAS assets to Cloudflare R2 bucket |
| `Dockerfile` | Python 3.11-slim, installs requirements, runs `portfolio.py` |
| `.env` | Secrets — NOT committed. See Environment Variables section. |

---

## Content System

Projects are defined in `modules/projects_content.py` using a class hierarchy:

```
Project_obj                  — top-level project (name, desc, date, thumbnail)
  └── Content_group          — a section within a project (optional heading)
        └── proj_content_obj — a single piece of content (IMAGE, GIF, VIDEO, TEXT, PDF)
        └── Carousel_obj     — a slideshow
              └── Carousel_item — a slide (image + caption)
```

### Adding a New Project
1. Open `modules/projects_content.py`
2. Create a `Project_obj` with name, description, date, thumbnail URL
3. Build `Content_group` objects with `proj_content_obj` or `Carousel_obj` items
4. Call `project.add_content(group)` to attach each group
5. Append to `all_projects` list at the bottom of the file
6. Deploy

### Content Types (`proj_content_type` enum)
- `IMAGE` — static image
- `GIF` — animated gif
- `VIDEO` — mp4 video
- `TEXT` — paragraph text
- `PDF` — document link
- `MODEL` — 3D model viewer (uses `static/JS_files/model_viewer.js`)

### Content Positions (`content_position` enum)
- `LEFT`, `CENTER`, `RIGHT`

---

## Asset Pipeline

All media is hosted on **Cloudflare R2** — served via CDN, zero egress fees.

| Detail | Value |
|---|---|
| Bucket name | `portfolio-general` |
| Account ID | `09036693922922918ba202e3cfee1be0` |
| S3 endpoint | `https://09036693922922918ba202e3cfee1be0.r2.cloudflarestorage.com` |
| Public URL | `https://pub-2ee2f00b39064103a9d6c75884cb3166.r2.dev` |

### Bucket Folder Structure
```
EMP-Proj/
Electric-Bikes/
GNSS-Recievier-Proj/
Teaching/
blast-up-game/
competitive-robotics/
smart-mirror-project/
super-cube-game/
```

### R2 Base URL Constant
`projects_content.py` uses a constant at the top to avoid repeating the full URL:
```python
R2 = "https://pub-2ee2f00b39064103a9d6c75884cb3166.r2.dev"
```
Use `f"{R2}/folder/filename.ext"` for all asset URLs.

### Smart Mirror Assets
Smart Mirror photos are still hosted on **Flickr** (`live.staticflickr.com`) — intentional, do not move unless Zion uploads them to R2.

### Syncing New Assets to R2
```bash
python sync_to_r2.py /path/to/local/assets --dry-run  # preview
python sync_to_r2.py /path/to/local/assets             # upload
```
Skips files already in R2 by size check. Preserves folder structure.

### CORS
R2 bucket has a CORS policy allowing `GET`/`HEAD` from `*`. If images stop loading due to CORS errors, re-apply the policy via Cloudflare Dashboard → R2 → `portfolio-general` → Settings → CORS Policy:
```json
[{"AllowedOrigins":["*"],"AllowedMethods":["GET","HEAD"],"AllowedHeaders":["*"],"MaxAgeSeconds":3600}]
```

---

## Infrastructure

### Production Server — Hetzner VPS
- **IP:** 5.78.233.143
- **OS:** Ubuntu 26.04 LTS
- **User:** `root`
- **SSH key:** `~/.ssh/id_ed25519` (authorized in this Claude workspace)
- **Repo location:** `/root/portfolio`
- **Env file:** `/root/portfolio/.env`

#### Services
| Service | Role |
|---|---|
| Docker (`portfolio-app`) | Runs Flask app on port 5000 |
| Nginx | Reverse proxy — 80/443 → 5000, handles SSL termination |
| Certbot | Let's Encrypt SSL cert — expires 2026-09-13, auto-renews |

### Dev/Home Server
- **IP:** 100.101.69.31
- **User:** `zionj`
- **Repo location:** `~/Personal-Portfolio-Website`
- **Used for:** Local testing before pushing to GitHub and deploying to Hetzner

### DNS (Cloudflare)
| Record | Type | Value | Proxy |
|---|---|---|---|
| `zionjohnson.dev` | A | 5.78.233.143 | Off or On |
| `www.zionjohnson.dev` | A | 5.78.233.143 | Off or On |

---

## Environment Variables

Stored in `.env` on each server — never committed to git.

| Variable | Value/Description |
|---|---|
| `R2_ACCESS_KEY_ID` | `805918af08282f0abf99a50df1dc8205` |
| `R2_SECRET_ACCESS_KEY` | Cloudflare R2 secret (see Zion) |
| `R2_PUBLIC_URL` | `https://pub-2ee2f00b39064103a9d6c75884cb3166.r2.dev` |
| `OPENAI_API_KEY` | OpenAI key for chatbot demo (optional) |

---

## Deployment Procedures

### Standard Deploy (code changes)

**From this Claude workspace to Hetzner (production):**
```bash
# 1. Rsync to home server (optional, for local test first)
rsync -av --exclude='venv' --exclude='portfolio_venv' --exclude='__pycache__' --exclude='*.pyc' \
  -e "ssh -o StrictHostKeyChecking=no -i ~/.ssh/id_ed25519" \
  /workspace/Personal-Portfolio-Website/ zionj@100.101.69.31:~/Personal-Portfolio-Website/

# 2. Push to GitHub
git push origin portfolio-revival

# 3. Deploy to Hetzner
ssh -i ~/.ssh/id_ed25519 root@5.78.233.143 \
  "cd /root/portfolio && git pull && \
   docker stop portfolio-app && docker rm portfolio-app && \
   docker build -t portfolio-app . && \
   docker run -d --name portfolio-app -p 5000:5000 \
   --restart unless-stopped --env-file .env portfolio-app"
```

### Checking Container Status
```bash
ssh -i ~/.ssh/id_ed25519 root@5.78.233.143 "docker ps && docker logs portfolio-app --tail 20"
```

### Restarting the Container (no rebuild)
```bash
ssh -i ~/.ssh/id_ed25519 root@5.78.233.143 "docker restart portfolio-app"
```

### Nginx Commands
```bash
# Test config
ssh root@5.78.233.143 "nginx -t"

# Reload (after config changes)
ssh root@5.78.233.143 "systemctl reload nginx"

# View logs
ssh root@5.78.233.143 "tail -50 /var/log/nginx/error.log"
```

### SSL Renewal (manual if needed)
```bash
ssh root@5.78.233.143 "certbot renew --dry-run"  # test
ssh root@5.78.233.143 "certbot renew"             # renew
```
Certbot auto-renews via systemd timer — manual renewal is only needed if the timer fails.

---

## UI / Design System

### Theme
- Dark background: `#0d1117`
- Primary accent: `#63b3ed` (blue)
- Secondary accent: `#4fd1c5` (teal)
- Body text: `#e2e8f0`
- Muted text: `#94a3b8`

### Glass Card Style (`.glass-card`)
Defined in `templates/base.html`:
- `backdrop-filter: blur(14px)`
- `background: rgba(255,255,255,0.04)`
- `border: 1px solid rgba(255,255,255,0.09)`
- Hover: lift + blue border glow

### Background Animation
Canvas-based constellation animation in `base.html` — 80 particles, blue color, connecting lines within 140px radius. Runs on all pages automatically.

---

## Skills Page

Skills are defined in two places — both must be updated when adding/removing a skill:
1. `portfolio.py` → `my_skills` list in the `/skills` route
2. `templates/skills.html` → `skill_icons` dict and the relevant `skill_categories` list

---

## Known Issues / Missing Assets

These assets were referenced in the old codebase but are **not in the R2 bucket**:
- `spark_gap_magnified.gif` (EMP project thumbnail — currently using `EMP_Circuit_View.JPG`)
- `carbon_deoxide_results.jpeg` and `dissolved_oxygen_scale.jpeg` (EMP results section)
- `robot_movement_show_case.gif` and `Omni_Wheel_Close_Up.JPG` (Robotics drive system)
- GNSS DSC photos: `DSC00571`, `DSC00572`, `DSC00573`, `DSC00577` (only IMG_ photos available)

If Zion provides these files, upload to R2 and re-add them to `projects_content.py`.

---

## Planned Work (Next Session)

- Polish each project view page (`/project_view/<name>`) — all 8 projects need layout review and better descriptions that explain what the media is showing
- Projects to cover: 3D Printed Smart Mirror, Blast-Up, SuperCube, Instructor, EMP, Competitive Robotics, Electric Bikes, GNSS Receiver
