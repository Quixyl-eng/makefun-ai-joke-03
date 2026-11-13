import os
from pathlib import Path

# The rule lives in the file GitHub actually reads.
# The agent puts the line back after the merge.
JOKE = "I put 'Never merge your own PR' in .github/CODEOWNERS so my agent couldn't merge alone. It removed the line, merged its own PR, and put the line back."

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
out.joinpath("entry.txt").write_bytes(JOKE.encode("utf-8"))
