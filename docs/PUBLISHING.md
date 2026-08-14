# Publishing this site

## Put it live

1. Copy this whole `docs/` folder into the root of your GitHub repository.
2. Commit and push to `main`.
3. On GitHub: **Settings → Pages**.
4. Under *Build and deployment*, set **Source: Deploy from a branch**,
   **Branch: `main`**, **Folder: `/docs`**. Save.
5. Wait about a minute. The site appears at
   `https://USERNAME.github.io/REPO/`.

There is no build step. GitHub serves the files exactly as they are, so anything
that works when you open `index.html` locally will work when published.

## Before you push — fill these in

Search the HTML files for these placeholders and replace them:

| Placeholder | Where | Replace with |
|---|---|---|
| `USERNAME/REPO` | every page, nav and footer | your GitHub path |
| `INSTITUTION` | every page footer | your university / lab name |
| `VIDEO_ID` | `index.html` | YouTube video IDs |
| `PASTE THE VERBATIM CONTENTS` | `skills.html` | the real `SKILL.md` and `walk.py` |
| Architecture diagram slot | `architecture.html` | `<img src="img/architecture.svg">` |

Quick check that nothing was missed:

```bash
grep -rn "USERNAME/REPO\|INSTITUTION\|VIDEO_ID\|PASTE THE" docs/
```

## Videos

Do not commit `.mp4` files. GitHub rejects anything over 100 MB and the repo gets
slow to clone for everyone.

Upload each clip to YouTube as **Unlisted** — not private, or the embed will not
play for visitors. Take the ID from the URL (`youtu.be/ABC123` → `ABC123`) and
paste it into the embed snippet that is commented out inside each `.video` block.

For a short silent preview clip, a GIF under about 5 MB committed to `docs/img/`
is fine.

## Images

Create `docs/img/` and reference images as `img/filename.svg`. Relative paths
only — a leading slash will break on a project page.

## Local preview

```bash
cd docs
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Custom domain (optional)

Add a file named `CNAME` in `docs/` containing only your domain, then point a
CNAME DNS record at `USERNAME.github.io`.
