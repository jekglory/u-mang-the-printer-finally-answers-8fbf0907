"""The Printer Finally Answers.

One line, spoken by the office printer to everyone staring at it,
mashing the print button, and thumping its side when it stops working.
It has counted every press. It has answered with silence fourteen times.
Now it answers in words.

The grader runs this program with no input and no network; it writes the
line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure standard library, deterministic: the same fixed line every run.
"""

import os

LINE = (
    # Deadpan count, deadpan count, then the comeback: the machine
    # claims the same professionalism as the human pressing the button.
    "You pressed print fourteen times. "
    "I printed nothing fourteen times. "
    "We are both professionals."
)


def main() -> None:
    if not 1 <= len(LINE) <= 240:
        raise SystemExit("line must be 1 to 240 characters")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
