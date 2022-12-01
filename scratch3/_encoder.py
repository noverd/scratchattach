import math

letters = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    " ",
    "a",
    "A",
    "b",
    "B",
    "c",
    "C",
    "d",
    "D",
    "e",
    "E",
    "f",
    "F",
    "g",
    "G",
    "h",
    "H",
    "i",
    "I",
    "j",
    "J",
    "k",
    "K",
    "l",
    "L",
    "m",
    "M",
    "n",
    "N",
    "o",
    "O",
    "p",
    "P",
    "q",
    "Q",
    "r",
    "R",
    "s",
    "S",
    "t",
    "T",
    "u",
    "U",
    "v",
    "V",
    "w",
    "W",
    "x",
    "X",
    "y",
    "Y",
    "z",
    "Z",
    "*",
    "/",
    ".",
    ",",
    "!",
    '"',
    "§",
    "$",
    "%",
    "_",
    "-",
    "(",
    "´",
    ")",
    "`",
    "?",
    "new line",
    "@",
    "#",
    "~",
    ";",
    ":",
    "+",
    "&",
    "|",
    "^",
    "'"
]


class Encoding:
    """
    Inner class for encoding / decoding strings.
    """
    def decode(self):
        self = str(self)
        outp = ""
        for i in range(math.floor(len(self) / 2)):
            letter = letters[int(f"{self[i * 2]}{self[i * 2 + 1]}")]
            outp = f"{outp}{letter}"
        return outp


    def encode(self):
        self = str(self)
        global encode_letters
        outp = ""
        for i in self:
            if i in letters:
                outp = f"{outp}{letters.index(i)}"
            else:
                outp += str(letters.index(" "))
        return outp
