# Deploying to Vercel

## Files to upload to GitHub

Upload **all** of these (not just `index.html`):

```
index.html
vercel.json
assets/
  dc-runtime.js
  mailerlite.js
```

Vercel will not work if you only upload `index.html` — the page loads JavaScript from the `assets/` folder.

## Web Analytics

The site includes Vercel Web Analytics scripts in `index.html`.

1. In the [Vercel dashboard](https://vercel.com), open your project → **Analytics** → click **Enable**.
2. Redeploy after enabling (so `/_vercel/insights/*` routes are available).
3. View visitors under **Analytics** once people hit the live site.

Analytics only collect data from the moment they are enabled — there is no historical backfill.

## Why the site showed raw JavaScript text

The previous version put ~60KB of JavaScript **inside** the HTML file. Browsers treat any `</script>` inside that block as the end of the script, which can leak the rest of the code as visible text on the page. Moving scripts to `assets/*.js` fixes that.

## Do not deploy for the live site

- `index (1).html` — Cursor bundle format (local editing only)
- `user interest.txt` / `host interest.txt` — MailerLite source embeds (already in the site)
- `unpack_for_deploy.py` / `fix_index_html.py` — build tools (optional to keep in repo)

## Vercel settings

- **Framework preset:** Other
- **Build command:** leave empty
- **Output directory:** `.` (root)

## After editing in Cursor

```bash
python unpack_for_deploy.py
```

Then commit and push:

- `index.html`
- `assets/dc-runtime.js`
- `assets/mailerlite.js`
