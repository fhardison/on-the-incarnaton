import glob
from greek_normalisation.utils import nfc
DIR_PATH = '../text/*.txt'


REPLACEMENTS = [
    ('\u1FBF', '\u2019'),
    ('\r\n', '\n'),
    ('\u0387', '\u00B7')
]

def process(ifile):
    print(ifile)
    text = ''
    with open(ifile, 'r', encoding="UTF-8") as f:
        text = f.read()
        for (t, r) in REPLACEMENTS:
            converted = text.replace(t,r)
        
    text = nfc(converted)
    with open(ifile, 'w', encoding="UTF-8") as f:
        f.write(text)
        
        
for f in glob.glob(DIR_PATH):
    process(f)