# Coast Charging Co — Website Elements

Exported brand kit pulled from the live website (`index.html` + `assets/`). Use these files for **MailerLite email templates**, social graphics, pitch decks, and other marketing.

## Folder structure

| Folder | Contents |
|--------|----------|
| `brand/` | Colors (`colors.json`) and fonts (`typography.json`) |
| `copy/` | All website headlines and body text (`website-copy.md`) |
| `icons/` | Logos and UI icons (SVG + PNG) |
| `photos/` | Hero and community images (JPG) |
| `media/` | Community loop video (MP4) |

## MailerLite brand setup

1. Open **Brand styles** in the template editor (right sidebar).
2. Add these brand colors (hex): `#16302B`, `#1587AE`, `#D9534A`, `#F0B429`, `#FFFDF8`
3. Set heading font to **Bricolage Grotesque** and body font to **Figtree** (see `brand/typography.json`).
4. Upload images from `photos/` and `icons/` — email clients handle JPG/PNG more reliably than SVG.

### Suggested email building blocks

| Site section | Assets to use |
|--------------|---------------|
| Header / logo | `icons/sun-logo.svg` + wordmark "Coast Charging Co" |
| Hero | `photos/hero-ebike-sunset.jpg` + hero copy from `copy/website-copy.md` |
| How it works | `icons/bicycle-red.svg`, `plug-charger.svg`, `battery-full.svg` |
| Community | `photos/community-video-poster.jpg` + community copy |
| Host CTA | `icons/red-umbrella.png` + host copy |
| Footer | `icons/sun-logo.svg`, contact email, dark bg `#16302B` |

## Files copied from site

- `icons/battery-full.svg`
- `icons/beach-umbrella-red.svg`
- `icons/bicycle-red-source.svg`
- `icons/bicycle-red.svg`
- `icons/bike-tagline.svg`
- `icons/birds-light.svg`
- `icons/birds-teal.svg`
- `icons/palm-dark.svg`
- `icons/palm-teal.svg`
- `icons/plug-charger.svg`
- `icons/red-umbrella.png`
- `icons/sun-logo.svg`
- `media/community-loop.mp4`
- `photos/community-video-poster.jpg`
- `photos/hero-ebike-rocks-alt.jpg`
- `photos/hero-ebike-sunset.jpg`

## Regenerating this folder

From the website project root:

```bash
python export_website_elements.py
```

This overwrites `website-elements/` with a fresh export.
