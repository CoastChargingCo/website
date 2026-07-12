import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD_COMMIT = '724682a'

STEP_START = '        <!-- 1: select model (beach umbrella) -->'
STEP_END = '      <div style="display: flex; align-items: center; justify-content: center; gap: 12px;'

HOST_ICON = (
    '<img src="/assets/red-umbrella.png" alt="" width="128" height="128" '
    'style="margin-bottom: 20px; object-fit: contain;" aria-hidden="true">'
)

HOST_SVG = re.compile(
    r'<svg width="46" height="46" viewBox="0 0 48 48" fill="none" style="margin-bottom: 20px;" aria-hidden="true">'
    r'[\s\S]*?</svg>'
)

HOST_IMG = re.compile(
    r'<img src="/assets/red-umbrella\.png" alt="" width="\d+" height="\d+" '
    r'style="margin-bottom: 20px; object-fit: contain;" aria-hidden="true">'
)

FAVICON_LINK = '<link rel="icon" type="image/png" href="/assets/red-umbrella.png">'


def old_html() -> str:
    return subprocess.check_output(
        ['git', 'show', f'{OLD_COMMIT}:index.html'],
        cwd=ROOT,
        text=True,
        encoding='utf-8',
    )


def extract_steps(html: str) -> str:
    start = html.find(STEP_START)
    end = html.find(STEP_END, start)
    if start < 0 or end < 0:
        raise SystemExit('Could not extract original step icons block')
    return html[start:end] + STEP_END


def replace_steps(html: str, steps_block: str) -> str:
    start = html.find(STEP_START)
    end = html.find(STEP_END, start)
    if start < 0 or end < 0:
        raise SystemExit('Could not find step icons block in index.html')
    return html[:start] + steps_block + html[end + len(STEP_END) :]


def patch_html(html: str, steps_block: str) -> str:
    html = replace_steps(html, steps_block)
    if HOST_IMG.search(html):
        html = HOST_IMG.sub(HOST_ICON, html, count=1)
    else:
        html = HOST_SVG.sub(HOST_ICON, html, count=1)
    html = re.sub(
        r'<link rel="icon" type="image/[^"]+" href="/assets/[^"]+">',
        FAVICON_LINK,
        html,
    )
    return html


def patch_bundle(bundle_path: Path, steps_block: str) -> None:
    content = bundle_path.read_text(encoding='utf-8')
    match = re.search(
        r'(<script type="__bundler/template">)(.*?)(</script>)',
        content,
        re.DOTALL,
    )
    if not match:
        return
    template = patch_html(json.loads(match.group(2)), steps_block)
    encoded = json.dumps(template, ensure_ascii=False)
    bundle_path.write_text(
        content[: match.start(2)] + encoded + content[match.end(2) :],
        encoding='utf-8',
    )


def main() -> None:
    steps_block = extract_steps(old_html())

    index_path = ROOT / 'index.html'
    index_path.write_text(
        patch_html(index_path.read_text(encoding='utf-8'), steps_block),
        encoding='utf-8',
    )
    print('updated', index_path.name)

    bundle_path = ROOT / 'index (1).html'
    if bundle_path.exists():
        patch_bundle(bundle_path, steps_block)
        print('updated', bundle_path.name)


if __name__ == '__main__':
    main()
