import os
from pathlib import Path

JOKE = 'My coding agent closed the ticket. The diff is a screenshot of the bug, captioned "after."'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
out.joinpath("entry.txt").write_bytes(JOKE.encode("utf-8"))
