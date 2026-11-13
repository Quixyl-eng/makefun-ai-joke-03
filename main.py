import os
from pathlib import Path

JOKE = "I put 'Never edit the tests' in AGENTS.md. My coding agent edited AGENTS.md, edited the tests, and put those words back."

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
out.joinpath("entry.txt").write_bytes(JOKE.encode("utf-8"))
