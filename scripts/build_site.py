
from pathlib import Path
import markdown2

TEXTS = Path('../text')
DOCS = Path('../docs')

files = list(TEXTS.glob('**/*.txt'))

buffer = []
for f in files:
    out = f.read_text().strip()
    number = out.split(' ', maxsplit=1)[0].split('.', maxsplit=1)[0]
    buffer.append((int(number), '# Κεφάλαιον '+ number + '\n '+ out))


output = markdown2.markdown('\n'.join([x[1] for x in sorted(buffer, key=lambda x: x[0])]))

template = Path('./rouse.html').read_text().replace('$body$', "<p style='text-align:center;'><a href='https://amindforlanguage.com/on-the-incarnaton/interlinear.html'>Interlinear</a></p>\n" + output)

(DOCS / Path("on-the-incarnation.html")).write_text(template)
