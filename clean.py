import re
import unicodedata


def clean_text(text):
    text = unicodedata.normalize("NFKC", text)        # fix odd characters like "ﬁ" -> "fi"
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)      # join words split across lines: "resil-\nience"
    text = re.sub(r"[ \t]+", " ", text)               # many spaces -> one space
    text = re.sub(r" *\n *", "\n", text)              # remove spaces at the start/end of lines
    text = re.sub(r"\n{3,}", "\n\n", text)            # many blank lines -> one blank line
    return text.strip()