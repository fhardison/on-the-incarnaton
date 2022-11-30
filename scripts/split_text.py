from pathlib import Path

ifile = Path("text/Athanasius - De Incarnatione Verbi (26-57).txt")

lines = ifile.read_text().splitlines()

for line in lines:
    if line.strip():
        number, _ = line.split(' ', maxsplit=1)
        chapter = number.replace(".1", '')
        Path(f'text/{chapter}-on-the-incarnation.txt').write_text(line)