"""Export website assets into website-elements/ for email templates and other uses."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "website-elements"
INDEX = ROOT / "index.html"
ICONS_SRC = Path(
    r"G:\My Drive\E-bike Charger\04_Marketing\Brand Assets (logos, colors, fonts)\Icons"
)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_if_exists(src: Path, dest: Path) -> bool:
    if not src.is_file():
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return True


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)

    # --- Copy raster / existing files ---
    copies = [
        (ROOT / "assets" / "red-umbrella.png", OUT / "icons" / "red-umbrella.png"),
        (ROOT / "assets" / "bicycle_red.svg", OUT / "icons" / "bicycle-red.svg"),
        (ROOT / "assets" / "media" / "hero.jpg", OUT / "photos" / "hero-ebike-sunset.jpg"),
        (ROOT / "assets" / "media" / "hero-alt.jpg", OUT / "photos" / "hero-ebike-rocks-alt.jpg"),
        (ROOT / "assets" / "media" / "community-poster.jpg", OUT / "photos" / "community-video-poster.jpg"),
        (ROOT / "assets" / "media" / "community.mp4", OUT / "media" / "community-loop.mp4"),
        (ICONS_SRC / "bicycle_red.svg", OUT / "icons" / "bicycle-red-source.svg"),
        (ICONS_SRC / "beach_umbrella._redsvg.svg", OUT / "icons" / "beach-umbrella-red.svg"),
    ]
    copied = []
    for src, dest in copies:
        if copy_if_exists(src, dest):
            copied.append(dest.relative_to(OUT).as_posix())

    # --- Standalone SVG icons (extracted from index.html) ---
    svgs = {
        "icons/sun-logo.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40" fill="none" aria-hidden="true">
  <circle cx="20" cy="20" r="8.5" fill="#F0B429"/>
  <g stroke="#E0913F" stroke-width="2.4" stroke-linecap="round">
    <line x1="20" y1="3" x2="20" y2="8"/>
    <line x1="20" y1="32" x2="20" y2="37"/>
    <line x1="3" y1="20" x2="8" y2="20"/>
    <line x1="32" y1="20" x2="37" y2="20"/>
    <line x1="8" y1="8" x2="11.5" y2="11.5"/>
    <line x1="28.5" y1="28.5" x2="32" y2="32"/>
    <line x1="8" y1="32" x2="11.5" y2="28.5"/>
    <line x1="28.5" y1="11.5" x2="32" y2="8"/>
  </g>
</svg>''',
        "icons/birds-teal.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="80" height="34" viewBox="0 0 80 34" fill="none" stroke="#0C6486" stroke-width="2" stroke-linecap="round" aria-hidden="true">
  <path d="M4 16 Q11 8 18 16 Q25 8 32 16"/>
  <path d="M40 24 Q46 17 52 24 Q58 17 64 24"/>
</svg>''',
        "icons/birds-light.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="90" height="40" viewBox="0 0 90 40" fill="none" stroke="#FBF6EC" stroke-width="2.4" stroke-linecap="round" aria-hidden="true">
  <path d="M4 20 Q13 10 22 20 Q31 10 40 20"/>
  <path d="M46 30 Q54 22 62 30 Q70 22 78 30"/>
</svg>''',
        "icons/palm-teal.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 160" fill="#0C6486" aria-hidden="true">
  <path d="M58 158 C 54 120, 60 90, 64 60 L72 60 C 74 92, 66 126, 66 158 Z"/>
  <path d="M64 58 C 40 38, 18 36, 4 46 C 22 40, 44 46, 63 60 Z"/>
  <path d="M64 58 C 58 26, 64 10, 74 2 C 68 22, 70 40, 68 60 Z"/>
  <path d="M66 58 C 92 34, 112 36, 118 50 C 98 40, 78 46, 66 60 Z"/>
  <path d="M63 60 C 40 58, 20 66, 10 80 C 30 64, 48 62, 62 62 Z"/>
  <path d="M67 60 C 90 58, 106 66, 114 82 C 96 66, 78 62, 66 62 Z"/>
  <circle cx="65" cy="58" r="5"/>
</svg>''',
        "icons/palm-dark.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 160" fill="#16221B" aria-hidden="true">
  <path d="M58 158 C 54 120, 60 90, 64 60 L72 60 C 74 92, 66 126, 66 158 Z"/>
  <path d="M64 58 C 40 38, 18 36, 4 46 C 22 40, 44 46, 63 60 Z"/>
  <path d="M64 58 C 58 26, 64 10, 74 2 C 68 22, 70 40, 68 60 Z"/>
  <path d="M66 58 C 92 34, 112 36, 118 50 C 98 40, 78 46, 66 60 Z"/>
  <path d="M63 60 C 40 58, 20 66, 10 80 C 30 64, 48 62, 62 62 Z"/>
  <path d="M67 60 C 90 58, 106 66, 114 82 C 96 66, 78 62, 66 62 Z"/>
  <circle cx="65" cy="58" r="5"/>
</svg>''',
        "icons/plug-charger.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="#1587AE" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M15 5v5"/>
  <path d="M25 5v5"/>
  <path d="M12 10h16v4a8 8 0 0 1 -16 0z" fill="#CDEAF2"/>
  <path d="M20 22v3"/>
  <path d="M20 25c0 6 10 5 11 11"/>
  <path d="M21.5 11.5l-3 4.5h3l-2 4" stroke="#1587AE" stroke-width="2.2"/>
</svg>''',
        "icons/battery-full.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="#2F8F55" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <rect x="6" y="13" width="25" height="15" rx="3.5"/>
  <rect x="9.5" y="16.5" width="18" height="8" rx="1.5" fill="#2F8F55" stroke="none"/>
  <rect x="32.5" y="17.5" width="3.5" height="6" rx="1.5" fill="#2F8F55" stroke="none"/>
</svg>''',
        "icons/bike-tagline.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none" stroke="#D9534A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <circle cx="9" cy="23" r="5"/>
  <circle cx="23" cy="23" r="5"/>
  <path d="M9 23l5-11h6M14 12l4 11M20 12h4"/>
</svg>''',
    }
    for rel, content in svgs.items():
        write(OUT / rel, content)
        copied.append(rel)

    colors = {
        "brandName": "Coast Charging Co",
        "domain": "coastchargingco.com",
        "email": "hello@coastchargingco.com",
        "palette": {
            "oceanTeal": {"hex": "#1587AE", "use": "Headlines, links, accent text"},
            "deepTeal": {"hex": "#0C6486", "use": "Buttons (host), birds, palms, nav accents"},
            "skyBlue": {"hex": "#8FCFE8", "use": "Hero gradient top"},
            "lightSky": {"hex": "#AEDDEE", "use": "Background gradients"},
            "paleSky": {"hex": "#BEE6F1", "use": "Host section background"},
            "softSky": {"hex": "#A6DAEC", "use": "Host section gradient"},
            "heroFrame": {"hex": "#C5E4EF", "use": "Hero photo frame background"},
            "coralRed": {"hex": "#D9534A", "use": "Primary CTA buttons, step 1 badge, bicycle icon"},
            "coralHover": {"hex": "#D9534F", "use": "Bicycle SVG stroke"},
            "sunGold": {"hex": "#F0B429", "use": "Sun logo, selection highlight"},
            "sunGlow": {"hex": "#FCE58A", "use": "Sun radial gradient"},
            "sunRay": {"hex": "#E0913F", "use": "Sun ray strokes"},
            "forestGreen": {"hex": "#2F8F55", "use": "Step 3 battery icon"},
            "plugFill": {"hex": "#CDEAF2", "use": "Charger plug icon fill"},
            "bodyText": {"hex": "#1B2A22", "use": "Primary body text"},
            "mutedText": {"hex": "#3A4740", "use": "Secondary body text"},
            "stepText": {"hex": "#47554A", "use": "How-it-works descriptions"},
            "hostHeading": {"hex": "#14322F", "use": "Host section headline"},
            "hostBody": {"hex": "#204A56", "use": "Host section body"},
            "footerBg": {"hex": "#16302B", "use": "Footer background"},
            "footerText": {"hex": "#CDD6CF", "use": "Footer body text"},
            "footerMuted": {"hex": "#A7B4AC", "use": "Footer links"},
            "footerDim": {"hex": "#7E8B83", "use": "Copyright line"},
            "cream": {"hex": "#FFFDF8", "use": "Light text on dark backgrounds"},
            "warmCream": {"hex": "#FFFDF6", "use": "Form input background"},
            "buttonText": {"hex": "#FFF8EE", "use": "Text on coral buttons"},
            "communityBg": {"hex": "#1A2E24", "use": "Community video section fallback"},
            "sandLight": {"hex": "#EBDDBB", "use": "Page gradient lower section"},
            "sandMid": {"hex": "#E4D0A4", "use": "Page gradient bottom"},
            "inputBorder": {"hex": "#C9B78E", "use": "Form field borders"},
            "inputFocus": {"hex": "#7FB6C8", "use": "Form field focus border"},
        },
        "gradients": {
            "pageBackground": "radial-gradient(900px 460px at 78% 60px, rgba(252,229,138,0.5) 0%, rgba(252,229,138,0) 60%), linear-gradient(180deg, #8FCFE8 0%, #AEDDEE 16%, #D8DBC0 40%, #EBDDBB 52%, #E4D0A4 100%)",
            "hostSection": "linear-gradient(180deg, #BEE6F1 0%, #A6DAEC 100%)",
            "communityOverlay": "linear-gradient(180deg, rgba(21,135,174,0.22) 0%, transparent 40%, rgba(20,32,26,0.62) 100%)",
            "heroPhotoOverlay": "linear-gradient(180deg, rgba(21,135,174,0.18), rgba(190,230,241,0.12) 68%, transparent)",
        },
        "mailerliteSuggestedBrandColors": ["#16302B", "#1587AE", "#D9534A", "#F0B429", "#FFFDF8"],
    }
    write(OUT / "brand" / "colors.json", json.dumps(colors, indent=2) + "\n")

    typography = {
        "headings": {
            "family": "Bricolage Grotesque",
            "googleFontsUrl": "https://fonts.google.com/specimen/Bricolage+Grotesque",
            "weights": [700, 800],
            "fallback": "sans-serif",
        },
        "body": {
            "family": "Figtree",
            "googleFontsUrl": "https://fonts.google.com/specimen/Figtree",
            "weights": [400, 500, 600],
            "fallback": "system-ui, sans-serif",
        },
        "mailerliteNote": "Set brand heading font to Bricolage Grotesque and body font to Figtree. MailerLite may substitute similar fonts in some clients.",
    }
    write(OUT / "brand" / "typography.json", json.dumps(typography, indent=2) + "\n")

    copy_md = """# Coast Charging Co — Website Copy

Use this text in emails, social posts, and other materials. Section names match the live site.

## Brand

- **Company name:** Coast Charging Co
- **Domain:** coastchargingco.com
- **Email:** hello@coastchargingco.com

---

## Navigation

- Host a station
- Get updates

---

## Hero

**Headline:** Powered by the Coast

**Subhead:** E-bike charging at the places you already love. Roll up, plug in, coast farther.

**CTA:** Subscribe (email signup)

---

## How it works

**Section headline:** Top up wherever you already stop.

**Section intro:** No charger to carry. No outlet to hunt for. Just roll up to a solar-powered station and top up in three simple steps, so range anxiety disappears and you ride more.

### Step 1 — Select your e-bike model
Pick your model so the station sends exactly the right charge.

### Step 2 — Plug in & lock up
Connect your bike and lock it in place. It's safe while it fills up.

### Step 3 — Walk away
Grab a coffee, take a swim, enjoy the day. Come back to a full battery.

**Tagline:** Everyone enjoys biking more than driving. Let's keep it that way.

---

## Community

**Headline:** Better rides are better together.

**Body:** Coast Charging is built for your community. We encourage everyone to take a bike ride with friends and worry less. Spontaneity is born when you aren't constrained. Be with your friends and have fun!

---

## Host a station

**Headline:** Become a Coast Charger Host.

**Body:** Parks, breweries, festivals, cafés: give riders a reason to stop, stay, and come back. It's off-grid and solar, so it can show up for an event, then roll on to the next one. No wiring, no permits, no infrastructure.

**CTA:** Subscribe (host interest signup)

---

## Footer

**Headline:** Powered by the Coast.

**Tagline:** Simple charging solutions.

**Explore links:** How it works · Why Coast · Host a station

**Contact:** hello@coastchargingco.com

**Copyright:** coastchargingco.com · © 2026
"""
    write(OUT / "copy" / "website-copy.md", copy_md)

    readme = f"""# Coast Charging Co — Website Elements

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

{chr(10).join(f'- `{p}`' for p in sorted(copied))}

## Regenerating this folder

From the website project root:

```bash
python export_website_elements.py
```

This overwrites `website-elements/` with a fresh export.
"""
    write(OUT / "README.md", readme)
    print(f"Exported to {OUT}")
    print(f"  {len(copied)} asset files")
    print("  brand/colors.json, brand/typography.json")
    print("  copy/website-copy.md, README.md")


if __name__ == "__main__":
    main()
