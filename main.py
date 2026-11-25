#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters -- make.fun bounty entry.

Writes one Wi-Fi network name (at most 32 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt and prints it. Fully deterministic, exit 0.
"""
import os

NAME = "Ex Took The Router, Not The Dog"


def main():
    assert 1 <= len(NAME) <= 32, "name must be 1-32 characters"
    assert NAME.strip() == NAME and NAME.strip(), "name must not be only whitespace"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NAME)
    print(NAME)


if __name__ == "__main__":
    main()
