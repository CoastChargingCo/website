import re
from pathlib import Path

NAV_SUN_26 = (
    '<svg width="26" height="26" viewBox="0 0 40 40" fill="none" aria-hidden="true">'
    '<circle cx="20" cy="20" r="8.5" fill="#F0B429"></circle>'
    '<g stroke="#E0913F" stroke-width="2.4" stroke-linecap="round">'
    '<line x1="20" y1="3" x2="20" y2="8"></line>'
    '<line x1="20" y1="32" x2="20" y2="37"></line>'
    '<line x1="3" y1="20" x2="8" y2="20"></line>'
    '<line x1="32" y1="20" x2="37" y2="20"></line>'
    '<line x1="8" y1="8" x2="11.5" y2="11.5"></line>'
    '<line x1="28.5" y1="28.5" x2="32" y2="32"></line>'
    '<line x1="8" y1="32" x2="11.5" y2="28.5"></line>'
    '<line x1="28.5" y1="11.5" x2="32" y2="8"></line>'
    '</g></svg>'
)

HEAD_META = (
    '<title>Coast Charging Co</title>\n'
    '<link rel="icon" type="image/png" href="/assets/red-umbrella.png">\n'
)

HOW_LABEL = (
    '      <span style="display: inline-block; font-weight: 600; color: #0C6486; '
    'letter-spacing: 0.06em; text-transform: uppercase; font-size: 13px; margin-bottom: 14px;">'
    'How it works</span>\n'
)


def patch_html(html: str) -> str:
    if '<title>Coast Charging Co</title>' not in html:
        html = html.replace(
            '<helmet>\n<link rel="preconnect"',
            '<helmet>\n' + HEAD_META + '<link rel="preconnect"',
            1,
        )
        html = html.replace(
            '<head>\n<meta charset',
            '<head>\n<title>Coast Charging Co</title>\n'
            '<link rel="icon" type="image/png" href="/assets/red-umbrella.png">\n<meta charset',
            1,
        )

    html = html.replace(HOW_LABEL, '', 1)

    html = re.sub(
        r'(<div style="display: flex; align-items: center; gap: 10px;">\s*)'
        r'<svg width="26" height="26" viewBox="0 0 40 40"[\s\S]*?</svg>',
        r'\1' + NAV_SUN_26,
        html,
        count=1,
    )

    return html
