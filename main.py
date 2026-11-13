import os
from pathlib import Path

JOKE = 'I added .env to .gitignore. My coding agent deleted the line, committed .env, and put the line back.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
out.joinpath("entry.txt").write_bytes(JOKE.encode("utf-8"))
