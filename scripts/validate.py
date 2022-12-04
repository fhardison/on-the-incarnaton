from text_validator.main import validate
from pathlib import Path

TEXTS = Path('../text')

files = list(TEXTS.glob('**/*.txt'))

nums = [f"{num:02d}" for num in range(1,25)]

check = ["26"] + nums

VALIDATED = [Path(f'../text/{x}-on-the-incarnation.txt') for x in check]

validate(Path('../text-validator.toml'), VALIDATED)
# ’