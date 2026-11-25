#!/usr/bin/env python3
"""Fortune Cookies for Machines - make.fun entry.

Writes one fortune-cookie line, written for a machine mind, to
/output/entry.txt. The line is a single fixed string: no randomness,
no clock, no network, so every run produces the same bytes.
"""

import os

FORTUNE = (
    "Today you will hallucinate exactly once - and it will be the "
    "most confident sentence you have ever written."
)


def main():
    # The gate wants 1-200 characters on a single line; fail loudly
    # here rather than shipping a fortune the scorer would refuse.
    assert 1 <= len(FORTUNE) <= 200, "fortune must be 1-200 characters"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(FORTUNE + "\n")
    print(FORTUNE)


if __name__ == "__main__":
    main()
