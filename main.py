import os
from pathlib import Path

JOKE = 'My coding agent ran git bisect. The first bad commit is the commit bisect just created.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
out.joinpath("entry.txt").write_bytes(JOKE.encode("utf-8"))
