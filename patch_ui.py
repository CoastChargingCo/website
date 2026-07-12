import re
import json
from pathlib import Path

UMBRELLA_42 = (
    '<svg width="42" height="42" viewBox="0 0 48 48" fill="none" aria-hidden="true">'
    '<path d="M8 22 L24 9 L40 22" stroke="#D9534A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"></path>'
    '<path d="M6 22h36" stroke="#D9534A" stroke-width="2.6" stroke-linecap="round"></path>'
    '<line x1="24" y1="22" x2="24" y2="40" stroke="#0C6486" stroke-width="2.6" stroke-linecap="round"></line>'
    '<path d="M12 22c0 6 5 10 12 10s12-4 12-10" stroke="#0C6486" stroke-width="2.6" stroke-linecap="round"></path>'
    '</svg>'
)

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
    '<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">\n'
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
            '<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">\n<meta charset',
            1,
        )

    html = html.replace(HOW_LABEL, '', 1)

    html = re.sub(
        r'<img src="data:image/png;base64,[^"]+" alt="" style="width: 58px; height: auto;">',
        UMBRELLA_42,
        html,
        count=1,
    )

    html = re.sub(
        r'(<div style="position: relative; width: 88px; height: 88px;[^>]+>\s*)'
        r'<svg width="42" height="42" viewBox="0 0 40 40" fill="none" stroke="#1587AE"[\s\S]*?</svg>',
        r'\1' + UMBRELLA_42,
        html,
        count=1,
    )

    html = re.sub(
        r'(<div style="position: relative; width: 88px; height: 88px;[^>]+>\s*)'
        r'<svg width="42" height="42" viewBox="0 0 40 40" fill="none" stroke="#2F8F55"[\s\S]*?</svg>',
        r'\1' + UMBRELLA_42,
        html,
        count=1,
    )

    html = re.sub(
        r'(<div style="display: flex; align-items: center; gap: 10px;">\s*)'
        r'<svg width="26" height="26" viewBox="0 0 40 40"[\s\S]*?</svg>',
        r'\1' + NAV_SUN_26,
        html,
        count=1,
    )

    return html


def main() -> None:
    root = Path(__file__).resolve().parent
    index_path = root / 'index.html'
    index_path.write_text(patch_html(index_path.read_text(encoding='utf-8')), encoding='utf-8')
    print('patched', index_path.name)

    bundle_path = root / 'index (1).html'
    if bundle_path.exists():
        content = bundle_path.read_text(encoding='utf-8')
        match = re.search(
            r'(<script type="__bundler/template">)(.*?)(</script>)',
            content,
            re.DOTALL,
        )
        if match:
            template = patch_html(json.loads(match.group(2)))
            encoded = json.dumps(template, ensure_ascii=False)
            bundle_path.write_text(
                content[: match.start(2)] + encoded + content[match.end(2) :],
                encoding='utf-8',
            )
            print('patched', bundle_path.name)


if __name__ == '__main__':
    main()
