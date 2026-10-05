from pathlib import Path

from parser import parse_pdf, parse_word, parse_html
from clean import clean_text


def parse_file(path):
    ext = path.suffix.lower()
    if ext == ".pdf":
        return parse_pdf(path)
    elif ext == ".docx":
        return parse_word(path)
    elif ext in (".html", ".htm"):
        return parse_html(path)
    else:
        return None


def main():
    file_name = input("Enter the file to parse: ").strip().strip('"')
    path = Path(file_name)

    if not path.exists():
        print(f"File not found: {path}")
        return

    text = parse_file(path)
    if text is None:
        print("Only PDF, Word (.docx) and HTML files are supported.")
        return

    cleaned = clean_text(text)

    output_path = path.with_name(f"{path.stem}_cleaned.txt")
    output_path.write_text(cleaned, encoding="utf-8")
    print(f"Saved {output_path} ({len(cleaned.split())} words)")


if __name__ == "__main__":
    main()