from pathlib import Path
from collections import Counter


def div(cons, _class=''):
    return f"<div class='{_class}'>{cons}</div>"


def span(cons, _class=''):
    return f"<span class='{_class}'>{cons}</span>"


def ul(cons, _class=''):
    return f"<ul class='{_class}'>{cons}</ul>"

def li(cons, _class=''):
    return f"<li class='{_class}'>{cons}</li>"

def word(text, lemma):
    return ul(li(span(text, 'word')) + li(span(lemma, 'lemma')))

HEADER = """ <head>
    <title>On the Incarnation</title>
    <meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css?family=Noto+Serif:400,400i,700&amp;subset=greek,greek-ext" rel="stylesheet">
    <link href="style.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/alpheios-components@latest/dist/style/style-components.min.css"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <link rel="stylesheet" href="https://unpkg.com/boltcss/bolt.min.css">  -->
  </head>
  <body class="index">
    <div class="container alpheios-enabled" lang="grc">
    <p style="text-align:center;"><a href="https://amindforlanguage.com/on-the-incarnaton/on-the-incarnation.html">Text</a></p>
"""

FOOTER = """</div> 
<script type="text/javascript">
  document.addEventListener("DOMContentLoaded", function(event) {
  import ("https://cdn.jsdelivr.net/npm/alpheios-embedded@latest/dist/alpheios-embedded.min.js").then(embedLib => {
      window.AlpheiosEmbed.importDependencies({ 
      mode: 'cdn'
      }).then(Embedded => {
      new Embedded({clientId: "thrax-grammar-fhard"}).activate();
      }).catch(e => {
      console.error(`Import of Alpheios embedded library dependencies failed: ${e}`)
      })

    
  }).catch(e => {
      console.error(`Import of Alpheios Embedded library failed: ${e}`)
  })
  });
</script>
</body>
</html>"""


print(HEADER)

norms = []
lemmas = []
words = 0
for line in Path("../analysis/analysis.txt").read_text().split('\n'):
    ref, text, norm, lemma = line.split(' ', maxsplit=3)
    words +=1
    norms.append(norm)
    lemmas.append(lemma)

lc = Counter(lemmas)
fc = Counter(norms)
lemmas_more_than_24 = [w for (w, i) in lc.most_common() if i > 9]

print(div(f"Total lemmas: {len(lc.keys())}", "count"))
print(div(f"Total lemmas occuring 10 times or more: {len(lemmas_more_than_24)}", "count"))
print(div(f"Total forms: {len(fc.keys())}", "count"))
print(div(f"Total words: {words}", "count"))

print("<div class='count-container'><ul>")
for (w, i) in lc.most_common():
    print(li(f"{i}: {w}", 'count-item'))

print("</ul></div>")

cdata = {}
c = 0
last_i = -1
print(lc.most_common()[0])
counts = dict(Counter(list([i for w, i in lc.most_common()])))
for i in reversed(range(0, lc.most_common()[0][1] + 1)):
    if i in counts:
        c += counts[i]
    cdata[i] = c


DATA = f"""
<script>
const countData = {cdata};""" + """
const inputBox = document.getElementById('count');
const output = document.getElementById('output');
function showResult() {

    var val = inputBox.value;
    console.log(countData[val]);
    output.textContent =  countData[val];
}
</script>
"""
# print(DATA)
print(FOOTER)
