from pathlib import Path


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

cur_chapter = '1'
cur_ref = '1'
buffer = []
for line in Path("../analysis/analysis.txt").read_text().split('\n'):
    ref, text, norm, lemma = line.split(' ', maxsplit=3)
    book, part = ref.split('.', maxsplit=1)
    if not f"{book}.{part}" == f"{cur_chapter}.{cur_ref}":
        print(div("Κεφαλαίον "+ cur_chapter + "." + cur_ref, 'chapter-heading')) 
        print(div(span(f"{cur_chapter}.{cur_ref} ", 'ref') + '\n'.join(buffer), 'line'))
        buffer = []
        cur_ref = part
        cur_chapter = book

    else:
        if norm == lemma:
            buffer.append(ul(li(span(text, 'word same')) + li(span(lemma, 'lemma same'))))
        else:
            buffer.append(word(text, lemma))

print(div(span(f"{cur_chapter}.{cur_ref} ", 'ref') + '\n'.join(buffer), 'line'))

print(FOOTER)
