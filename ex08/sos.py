import sys
import string

alphabet = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--.."
}

entree = ""
morse = ""
if (len(sys.argv) >= 2):
    for arg in sys.argv[1:]:
        arg2 = arg.strip().translate(str.maketrans('', '', " "))
        if not(arg2.strip().isalnum()):
            print("ERROR")
            sys.exit()
        entree = entree + " " + arg.strip()
    for c in entree.strip():
        if c == " ":
            morse += " / "
        else:
            morse += " " + alphabet[c.lower()]
    print(morse)
else:
    print("ERROR")
    sys.exit()
