import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def parse_mailerlite_form(path: Path) -> str:
    content = path.read_text(encoding='utf-8')
    m = re.search(
        r'(<div id="mlb2-\d+" class="ml-form-embedContainer.*?</div>)\s*(?:\n\s*){1,3}<script>',
        content,
        re.DOTALL,
    )
    return m.group(1).strip()

host_form = parse_mailerlite_form(ROOT / 'host interest.txt')
html = (ROOT / 'index.html').read_text(encoding='utf-8')

anchor = 'No wiring, no permits, no infrastructure.</p>'
host_start = html.find('<section id="host"')
host_end = html.find('<!-- ===================== FOOTER ===================== -->', host_start)
if host_start < 0 or host_end < 0:
    raise SystemExit('Could not locate host section')

section = html[host_start:host_end]
anchor_pos = section.find(anchor)
if anchor_pos < 0:
    raise SystemExit('Could not find host intro paragraph')
cut = anchor_pos + len(anchor)

new_section = (
    section[:cut]
    + '\n      <div id="host-interest-signup" style="max-width: 520px; margin: 0 auto;">\n'
    + host_form
    + '\n      </div>\n    </div>\n  </section>\n\n  '
)

html = html[:host_start] + new_section + html[host_end:]
(ROOT / 'index.html').write_text(html, encoding='utf-8', newline='\n')

forms = len(re.findall(r'<div id="mlb2-43550887"', html))
print('Fixed index.html — host form divs:', forms)
