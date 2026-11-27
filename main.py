import os

# One short thank-you text, written literally, so the output is the same on every run.
TEXT = "Thank you. You have read all day with the window shut, so I have opened it for you. Cool night air comes in over the sill, carrying the smell of wet grass from the garden below. Lean back and breathe it in. It will still be here when the next page comes, and the one after that, fresh each time you need it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
