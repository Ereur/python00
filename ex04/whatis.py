import sys


def main():
    """Check if a number is odd or even."""
    args = sys.argv[1:]
    assert len(args) <= 1, "more than one argument is provided"
    if len(args) == 1:
        assert args[0].lstrip('-').isdigit(), "argument is not an integer"
        number = int(args[0])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
