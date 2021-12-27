import glob
from greek_normalisation.utils import nfc
DIR_PATH = '../text/*.txt'

def process(ifile):
    print(ifile)
    text = ''
    with open(ifile, 'r', encoding="UTF-8") as f:
        text = f.read()
        converted = text.replace('\u1FBF', '\u2019')
        
    text = nfc(converted)
    with open(ifile, 'w', encoding="UTF-8") as f:
        f.write(text)
        
        
for f in glob.glob(DIR_PATH):
    process(f)