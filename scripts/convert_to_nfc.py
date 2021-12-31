import glob
from greek_normalisation.utils import nfc
import os.path
import subprocess
import sys


DIR_PATH = os.path.join(os.path.dirname(__file__), '..', 'text')


REPLACEMENTS = [
    ('\u1FBF', '\u2019'),
    ('\r\n', '\n'),
    ('\u0387', '\u00B7'),
]


def process(ifile):
    print(ifile)
    text = ''
    with open(ifile, 'r', encoding="UTF-8") as f:
        text = f.read()
        for (t, r) in REPLACEMENTS:
            text = text.replace(t,r)
        
    text = nfc(text)
    with open(ifile, 'w', encoding="UTF-8") as f:
        f.write(text)
    convert_line_endings(ifile)


def convert_line_endings(ifile):    
    text = ''
    with open(ifile, 'rb') as f:
        text = f.read()                
    text = text.replace(b'\r\n', b'\n')
    with open(ifile, 'wb') as f:
        f.write(text)


FILES = list(glob.glob(DIR_PATH + '\\*.txt'))


def process_files():
    for f in FILES:
        process(f)


if len(sys.argv) > 1 and '-v' in sys.argv[1]:
    args = ['validate-text', os.path.join(os.path.dirname(__file__),'..', 'text-validator.toml')]
    args.extend(FILES)
    subprocess.run(args)
else:
    process_files()
