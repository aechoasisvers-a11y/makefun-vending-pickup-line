"""One Line, One Minute: The Vending Machine Pickup Line.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt.
"""

import os

TEXT = (
    "I don't have a heart, just coils, but they spin a little faster "
    "when you walk by. Press B7 and I'll drop something sweet. "
    "No exact change required."
)


def main():
    # Gate self-checks: 1-200 chars, not whitespace only, one line.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be whitespace only"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT == TEXT.strip(), "entry must not start or end with spaces"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Post-write verification: prove the bytes on disk are exactly the
    # intended text, so a silent write failure or encoding slip fails
    # loudly here instead of reaching the judge.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == TEXT, "entry.txt decoded text mismatch"
    assert raw == TEXT.encode("utf-8"), "entry.txt byte mismatch"
    assert len(raw) == len(TEXT.encode("utf-8")), "entry.txt length mismatch"


if __name__ == "__main__":
    main()
