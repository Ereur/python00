import sys
from ft_filter import ft_filter


def main():
    """Filter words from a string by length."""
    args = sys.argv[1:]
    assert len(args) == 2, "the arguments are bad"
    assert args[1].isdigit(), "the arguments are bad"
    string = args[0]
    n = int(args[1])
    result = list(ft_filter(lambda word: len(word) > n, string.split()))
    print(result)


if __name__ == "__main__":
    main()
