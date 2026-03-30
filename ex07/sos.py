import sys


MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}


def main():
    """Encode a string into Morse code."""
    args = sys.argv[1:]
    assert len(args) == 1, "the arguments are bad"
    text = args[0]
    result = []
    for char in text.upper():
        assert char in MORSE_DICT, "the arguments are bad"
        result.append(MORSE_DICT[char])
    print(' '.join(result))


if __name__ == "__main__":
    main()
