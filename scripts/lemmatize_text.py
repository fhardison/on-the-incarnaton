from pathlib import Path
from cltk.lemmatize.grc import GreekBackoffLemmatizer
# from cltk.corlus.utils.formatter import cltk_normalize
from cltk.alphabet.text_normalization import cltk_normalize
from cltk.alphabet import grc
import re

ofile = Path('../analysis/analysis.txt')
lemmatizer = GreekBackoffLemmatizer()
output = []
def clean(x):
    return re.sub(r"[.?;!)(, ̓'·•]", '', x)

for f in sorted(Path('../text/').glob('*.txt')):
    for line in f.read_text().split('\n'):
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue
        elif "END" in line: 
            break
        else:
            ref, rest = line.split(' ', maxsplit=1)
            sent = grc.normalize_grc(rest) #cltk_normalize(line)
            results = lemmatizer.lemmatize([clean(x.lower()) for x in sent.split()])        
            for ((norm, lem), text) in list(zip(results, sent.split())):
                output.append((ref, text, norm, lem))

def fix_clipped_words(xs):
    out = []
    texts = []
    lemmas = []
    norms = []
    cur_ref = ''
    for (ref, text, norm, lem) in xs:
        if text == ' ̓' or lem == '':  
            out[-1][1] += text.strip()
            continue
        else:
           out.append([ref, text, norm, lem]) 

    return [f"{ref} {text} {norm} {lem}" for (ref, text, norm, lem) in out]
ofile.write_text('\n'.join(fix_clipped_words(output)))


