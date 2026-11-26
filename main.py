#!/usr/bin/env python3
"""Entry for make.fun: The One-Line Cat Joke That Lands.

The entry is a single joke about cats, one line under 200
characters. The joke is about the oldest transaction in the
human-cat relationship: the human bought an expensive bed,
with washable covers and a design brief, and the cat has
reviewed it carefully and chosen the box it arrived in. The
box is not a compromise or a second choice; in the cat's
published opinion it is the actual product, and the bed was
the packaging, which the human may keep as a souvenir,
preferably somewhere the cat can sit on it instead.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I bought my cat a bed so expensive it had a warranty; "
    "she reviewed it thoroughly and now sleeps in the box "
    "it came in."
)

# The bed is currently used to store the box's paperwork.
# The cat rates the box five stars and the bed 'a nice try'.
BOX_STARS = 5


def render_entry() -> str:
    """Return the joke exactly as it will be told."""
    return ENTRY_TEXT


def one_line_cat_joke(text: str) -> bool:
    """Confirm the joke is one line under 200 characters."""
    return "\n" not in text and len(text) < 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert one_line_cat_joke(text), "one line, under 200 characters"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
