
from pathlib import Path
import re
import base64

file = Path("index.html")
html = file.read_text(encoding="utf-8")

pattern = r"<script>([\s\S]*?)</script>"
match = re.search(pattern, html, re.I)

if not match:
    raise Exception("Could not find the inline script!")

js = match.group(1)
encoded = base64.b64encode(js.encode()).decode()

replacement = (
    '<script>(()=>{'
    f'const s=atob("{encoded}");'
    '(0,eval)(s);'
    '})();</script>'
)

html = html[:match.start()] + replacement + html[match.end():]
file.write_text(html, encoding="utf-8")

print("MintGPT JavaScript obfuscated!")
