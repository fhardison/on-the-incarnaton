from text_validator.main import validate
from pathlib import Path
from greek_normalisation.utils import nfc

TEXTS = Path('../text')

files = list(TEXTS.glob('**/*.txt'))
# for f in files:
#     out = f.read_text().strip()
#     f.write_text(out + "\n")
# exit()

nums = [f"{num:02d}" for num in range(1,31)]

check = nums

VALIDATED = [Path(f'../text/{x}-on-the-incarnation.txt') for x in check]

validate(Path('../text-validator.toml'), VALIDATED)
# ’