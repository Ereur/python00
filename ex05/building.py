import sys


def main():
    """Analyze a text and count character types."""
    args = sys.argv[1:]
    assert len(args) <= 1, "more than one argument is provided"
    if len(args) == 0:
        print("What is the text to count?")
        text = sys.stdin.readline()
    else:
        text = args[0]
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation = sum(1 for c in text if c in punct)
    spaces = sum(1 for c in text if c == ' ')
    digits = sum(1 for c in text if c.isdigit())
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
