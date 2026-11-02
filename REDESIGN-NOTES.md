# Home page redesign: notes for the founders

Branch: `redesign` (made from `main`, which matches the live site at commit 7d581a1).

## What changed

- Plain HTML + one stylesheet (`assets/css/site.css`) + one small script (`assets/js/site.js`). No `dc-runtime.js`, no React from unpkg, no blank page if a script fails.
- `index.html` went from about 1 MB to about 15 KB. Fonts load from Google Fonts, which fixes the Figtree 404 (body text was falling back to a system font).
- Both MailerLite forms keep their container IDs/classes, form actions, `fields[email]`, hidden `ml-submit` and `anticsrf` inputs, `row-form` / `row-success` blocks, `assets/mailerlite.js` and the `webforms.min.js` script. They now share one style.
- Removed: fixed bird layer, the seven margin umbrellas, the hero sun's glow and bobbing, the social circles that weren't links.
- Added: meta description, Open Graph / Twitter tags, canonical URLs, focus styles, reduced-motion support for the video.
- New section "Meet the Coast Charger" (founder-written copy, no photo) sits between the hero and How it works.

## Before you merge

1. Push the branch and open the Vercel preview URL.
2. Test both forms on the preview: submit a real address, confirm the on-page "Thank you!" message replaces the form, and that the subscriber lands in the right MailerLite group.
3. Check MailerLite: is double opt-in still on for both forms?
4. About and Roadmap are hidden: their links are removed from the nav and footer, and vercel.json temporarily redirects /about and /roadmap to the home page. To bring them back, fill in about.html / roadmap.html, re-add the links, and delete the two redirects.

Files no longer used once this is merged (safe to delete later): `assets/dc-runtime.js`, `assets/media-loop.js`, `assets/site-nav.css`, `assets/site-nav.js`, and the umbrella/sun PNGs except `red-umbrella.png` (favicon).

## Copy and claims to decide (live copy kept as written)

| Line | Issue |
|---|---|
| "We are building a network of Coast Chargers across San Diego" | A company-owned network is a possible late stage, not committed. |
| "Get notified when a Coast Charger opens near you" | Implies public locations are coming; next step is a closed pilot. |
| "Just ride up", the three self-serve steps, "come back to a full battery!" | Describes walk-up, unattended charging and a guaranteed result. The pilot has an operator at every session. |
| "hosting a charger at your business" | Permanent host offer isn't approved; managed event activations come first. |
| "There's no wiring to run, no permits to pull" (host welcome email) | Unsupported approval claim. Not used on the site; fix the email. |
| "Coast Charging is built for your community" | Shortens the name; strategy says not to shorten in formal brand language. |
| "Coast Charging Co" vs "Coast Charging Co." | Pick one. The site currently uses no period everywhere. |
| "Everyone enjoys biking more than driving." | Absolute claim; reads as opinion, low risk, but worth a look. |
| How-it-works steps | Uneven lengths and no supporting text. Step 1 "Plug in your bike" and step 2 "Turn on the charging with a switch" are fine; step 3 carries the guarantee issue above. |
| "Meet the Coast Charger": "Each station can charge 5 e-bikes at once", "portable", "set it up at a coffee shop, farmer's market, or the beach" | The built prototype charges two bikes; five is the goal. Portability and public set-up imply readiness the strategy says not to claim yet. |
| Meta description, host field placeholder | New copy written for the redesign. Uses only approved claims; please approve or edit. |

## Open questions

- Should About and Roadmap stay in the nav while unfinished?
- Real social links, if any? (Icons removed until then.)
- Is MailerLite double opt-in off now?
- Should public copy move to closed-pilot language now?
