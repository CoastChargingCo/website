# Deploying to Vercel

The site is plain static HTML. There is no build step.

## Files

```
index.html, about.html, roadmap.html
vercel.json            (clean URLs: /about serves about.html)
assets/css/site.css    (all styles and design tokens)
assets/js/site.js      (phone menu + video loop)
assets/mailerlite.js   (form success handlers; names must match the form IDs)
assets/media/          (hero photo, community video and poster)
assets/red-umbrella.png (favicon)
```

## Steps

1. Commit and push to GitHub. Every branch gets a Vercel preview URL; `main` deploys to coastchargingco.com.
2. Vercel settings: Framework preset "Other", build command empty, output directory `.`.
3. Vercel Web Analytics stays enabled through the script tag in each page's `<head>`.

## Editing

- Colors, type sizes, spacing and radii are CSS variables at the top of `assets/css/site.css`.
- Do not change the MailerLite form IDs, classes, `action` URLs or hidden inputs. Restyle them in `site.css` instead.
