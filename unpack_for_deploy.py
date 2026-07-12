import base64
import gzip
import json
import re
import subprocess
from pathlib import Path

from patch_ui import patch_html
from fix_umbrella_icons import extract_steps, old_html, patch_html as patch_umbrella_icons

ROOT = Path(__file__).resolve().parent
BUNDLE_PATH = ROOT / 'index (1).html'
OUTPUT_PATH = ROOT / 'index.html'
ASSETS_DIR = ROOT / 'assets'

MAILerlite_LOADER = '''
<script src="/assets/mailerlite.js"></script>
<script src="https://groot.mailerlite.com/js/w/webforms.min.js?v83147fa8ce2d95cb73ece7f28b469519" type="text/javascript"></script>
'''

MAILerlite_JS = '''function ml_webform_success_43550367() {
  var root = document.querySelector('.ml-subscribe-form-43550367');
  if (!root) return;
  var success = root.querySelector('.row-success');
  var form = root.querySelector('.row-form');
  if (success) success.style.display = '';
  if (form) form.style.display = 'none';
}
function ml_webform_success_43550887() {
  var root = document.querySelector('.ml-subscribe-form-43550887');
  if (!root) return;
  var success = root.querySelector('.row-success');
  var form = root.querySelector('.row-form');
  if (success) success.style.display = '';
  if (form) form.style.display = 'none';
}
'''


def decode_asset(entry: dict) -> bytes:
    raw = base64.b64decode(entry['data'])
    if entry.get('compressed'):
        raw = gzip.decompress(raw)
    return raw


def to_data_url(entry: dict) -> str:
    data = decode_asset(entry)
    mime = entry['mime']
    encoded = base64.b64encode(data).decode('ascii')
    return f'data:{mime};base64,{encoded}'


def externalize_dc_runtime(html: str, dc_runtime_js: str) -> str:
    """Keep dc-runtime out of inline HTML so </script> sequences cannot break the page."""
    ASSETS_DIR.mkdir(exist_ok=True)
    (ASSETS_DIR / 'dc-runtime.js').write_text(dc_runtime_js, encoding='utf-8', newline='\n')
    (ASSETS_DIR / 'mailerlite.js').write_text(MAILerlite_JS, encoding='utf-8', newline='\n')

    # Replace inline dc-runtime (from bundle inlining or prior unpack)
    html = re.sub(
        r'<script src="[^"]*">\s*// GENERATED from dc-runtime.*?</script>',
        '<script src="/assets/dc-runtime.js"></script>',
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'<script>\s*// GENERATED from dc-runtime.*?</script>',
        '<script src="/assets/dc-runtime.js"></script>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    # Replace inline MailerLite callbacks if present
    html = re.sub(
        r'<script>\s*function ml_webform_success_43550367\(\).*?</script>\s*(?=<script src="https://groot\.mailerlite\.com)',
        '<script src="/assets/mailerlite.js"></script>\n',
        html,
        count=1,
        flags=re.DOTALL,
    )

    return html


def main() -> None:
    content = BUNDLE_PATH.read_text(encoding='utf-8')

    manifest_match = re.search(
        r'<script type="__bundler/manifest">(.*?)</script>',
        content,
        re.DOTALL,
    )
    template_match = re.search(
        r'<script type="__bundler/template">(.*?)</script>',
        content,
        re.DOTALL,
    )
    if not manifest_match or not template_match:
        raise SystemExit('Could not find bundled manifest/template')

    manifest = json.loads(manifest_match.group(1))
    template = json.loads(template_match.group(1))

    dc_runtime_js = None
    for uuid, entry in manifest.items():
        if entry['mime'] == 'text/javascript':
            dc_runtime_js = decode_asset(entry).decode('utf-8')
            template = template.replace(
                f'<script src="{uuid}"></script>',
                '<script src="/assets/dc-runtime.js"></script>',
            )
        else:
            template = template.replace(uuid, to_data_url(entry))

    if not dc_runtime_js:
        raise SystemExit('Could not find dc-runtime JavaScript in manifest')

    template = re.sub(r'\s+integrity="[^"]*"', '', template, flags=re.I)
    template = re.sub(r'\s+crossorigin="[^"]*"', '', template, flags=re.I)

    if '</body>' in template:
        template = template.replace('</body>', MAILerlite_LOADER + '\n</body>', 1)
    else:
        template += MAILerlite_LOADER

    template = externalize_dc_runtime(template, dc_runtime_js)
    template = patch_html(template)
    template = patch_umbrella_icons(template, extract_steps(old_html()))

    OUTPUT_PATH.write_text(template, encoding='utf-8', newline='\n')
    print(f'Wrote {OUTPUT_PATH} ({len(template):,} chars)')
    print(f'Wrote {ASSETS_DIR / "dc-runtime.js"} ({len(dc_runtime_js):,} chars)')
    print(f'Wrote {ASSETS_DIR / "mailerlite.js"}')

    subprocess.run(['python', str(ROOT / 'fix_index_html.py')], check=True)


if __name__ == '__main__':
    main()
