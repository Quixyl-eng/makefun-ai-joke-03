import os
from pathlib import Path

JOKE = 'My coding agent retried the charge. The customer got three copies of the stack trace, titled "your receipt."'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
out.joinpath("entry.txt").write_bytes(JOKE.encode("utf-8"))
