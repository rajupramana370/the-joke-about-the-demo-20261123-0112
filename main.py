"""Entry for make.fun competition the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic,
no network, no input.
"""

import os

JOKE = (
    "My agent's commit for the demo fix says just 'fixed' "
    "\u2014 412 files changed, nothing explained, confidence: absolute."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
