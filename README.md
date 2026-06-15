# Zion Johnson — Personal Portfolio

A full-stack personal portfolio web application built with Python and Flask, containerized with Docker, and deployed on self-hosted infrastructure. The site showcases engineering projects across electrical engineering, embedded systems, software development, and game development.

**Live at:** `http://100.101.69.31:5000`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11, Flask |
| Templating | Jinja2 |
| Frontend | Bootstrap 5, Vanilla JS, HTML5 Canvas |
| Asset Storage | Cloudflare R2 (S3-compatible CDN) |
| Containerization | Docker |
| Deployment | Rsync + Docker on self-hosted Linux server |
| Environment | python-dotenv |

---

## Features

- **Dynamic project content system** — Projects, content groups, carousels, and media objects are defined in Python and rendered through a custom `Project_obj` / `Content_group` class hierarchy, making it easy to add or restructure projects without touching templates.
- **Cloudflare R2 asset hosting** — All media (images, GIFs, videos) is served from a Cloudflare R2 bucket for global CDN delivery with zero egress fees. Includes a `sync_to_r2.py` script for pushing local assets to the bucket.
- **Frosted glass UI** — Cards and navigation use `backdrop-filter: blur` with semi-transparent backgrounds for a modern glass aesthetic, keeping the dark theme intact.
- **Canvas particle animation** — A constellation-style background animation is rendered on an HTML5 `<canvas>` element, with 80 drifting particles connected by proximity lines. Runs at 60fps with no external dependencies.
- **Containerized deployment** — The entire app runs in a Docker container with an `--env-file` for secret injection, making it portable and reproducible across environments.
- **Experimental features** — Includes a GPS car tracker stream endpoint, an item tracker app with a configurable count/goal system, and an OpenAI GPT chatbot integration (used in the Smart Mirror project demo).

---

## Project Structure

```
├── portfolio.py              # Flask app, routes, OpenAI integration
├── modules/
│   ├── project.py            # Project, Content_group, Carousel data models
│   ├── projects_content.py   # All project content definitions
│   └── item_tracker_app/     # Item tracker module
├── templates/
│   ├── base.html             # Layout, navbar, glass styles, canvas animation
│   ├── index.html            # Hero landing page
│   ├── projects.html         # Project card grid
│   ├── project_view.html     # Individual project page renderer
│   ├── skills.html           # Skills page with category grouping
│   └── ...
├── static/
│   └── JS_files/             # 3D model viewer JS
├── sync_to_r2.py             # NAS → Cloudflare R2 asset sync script
├── Dockerfile
└── requirements.txt
```

---

## Local Development

**Prerequisites:** Python 3.11+, pip

```bash
# Clone the repo
git clone <repo-url>
cd Personal-Portfolio-Website

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Fill in R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_PUBLIC_URL, OPENAI_API_KEY

# Run the app
python portfolio.py
```

App will be available at `http://localhost:5000`.

---

## Docker Deployment

```bash
# Build the image
docker build -t portfolio-app .

# Run the container
docker run -d \
  --name portfolio-app \
  -p 5000:5000 \
  --restart unless-stopped \
  --env-file .env \
  portfolio-app
```

---

## Asset Sync (Cloudflare R2)

Assets are stored in the `portfolio-general` R2 bucket and served via the public `r2.dev` URL. To sync a local folder of assets to R2:

```bash
# Preview what would be uploaded
python sync_to_r2.py /path/to/assets --dry-run

# Upload (skips files already in R2 by size check)
python sync_to_r2.py /path/to/assets
```

---

## Environment Variables

| Variable | Description |
|---|---|
| `R2_ACCESS_KEY_ID` | Cloudflare R2 API access key |
| `R2_SECRET_ACCESS_KEY` | Cloudflare R2 API secret |
| `R2_PUBLIC_URL` | Public r2.dev URL for the asset bucket |
| `OPENAI_API_KEY` | OpenAI API key (optional, powers the chatbot demo) |

---

## Author

**Zion Johnson** — Self-taught programmer and electrical engineer. K12 STEM instructor teaching circuit building and microcontroller programming on behalf of a technical college.

- Email: zspynet22@icloud.com
