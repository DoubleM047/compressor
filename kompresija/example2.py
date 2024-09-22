import pyae
from decimal import getcontext

# Example for encoding a simple text message using the PyAE module.

# Create the frequency table.
frequency_table = {
  " ": 0.01,
  "!": 0.01,
  "\"": 0.01,
  "#": 0.01,
  "$": 0.01,
  "%": 0.01,
  "&": 0.01,
  "'": 0.01,
  "(": 0.01,
  ")": 0.01,
  "*": 0.01,
  "+": 0.01,
  ",": 0.01,
  "-": 0.01,
  ".": 0.01,
  "/": 0.01,
  "0": 0.01,
  "1": 0.01,
  "2": 0.01,
  "3": 0.01,
  "4": 0.01,
  "5": 0.01,
  "6": 0.01,
  "7": 0.01,
  "8": 0.01,
  "9": 0.01,
  ":": 0.01,
  ";": 0.01,
  "<": 0.01,
  "=": 0.01,
  ">": 0.01,
  "?": 0.01,
  "@": 0.01,
  "A": 0.01,
  "B": 0.01,
  "C": 0.01,
  "D": 0.01,
  "E": 0.01,
  "F": 0.01,
  "G": 0.01,
  "H": 0.01,
  "I": 0.01,
  "J": 0.01,
  "K": 0.01,
  "L": 0.01,
  "M": 0.01,
  "N": 0.01,
  "O": 0.01,
  "P": 0.01,
  "Q": 0.01,
  "R": 0.01,
  "S": 0.01,
  "T": 0.01,
  "U": 0.01,
  "V": 0.01,
  "W": 0.01,
  "X": 0.01,
  "Y": 0.01,
  "Z": 0.01,
  "[": 0.01,
  "\\": 0.01,
  "]": 0.01,
  "^": 0.01,
  "_": 0.01,
  "`": 0.01,
  "a": 0.01,
  "b": 0.01,
  "c": 0.01,
  "d": 0.01,
  "e": 0.01,
  "f": 0.01,
  "g": 0.01,
  "h": 0.01,
  "i": 0.01,
  "j": 0.01,
  "k": 0.01,
  "l": 0.01,
  "m": 0.01,
  "n": 0.01,
  "o": 0.01,
  "p": 0.01,
  "q": 0.01,
  "r": 0.01,
  "s": 0.01,
  "t": 0.01,
  "u": 0.01,
  "v": 0.01,
  "w": 0.01,
  "x": 0.01,
  "y": 0.01,
  "z": 0.01, 
  "{": 0.01,
  "|": 0.01,
  "}": 0.01,
  "~": 0.01,
  "\n": 0.01
}
# Create an instance of the ArithmeticEncoding class.
AE = pyae.ArithmeticEncoding(frequency_table, 
                             save_stages=True)

# Default precision is 28. Change it to do arithmetic operations with larger/smaller numbers.
getcontext().prec = 200000

x = open("input.txt", "r").readlines()
original_msg = ""

for i in x:
    original_msg += i


# Encode the message
encoded_msg, encoder , interval_min_value, interval_max_value = AE.encode(msg=original_msg, 
                                                                          probability_table=AE.probability_table)

#print(encoded_msg)

# Decode the message
decoded_msg, decoder = AE.decode(encoded_msg=encoded_msg, 
                                 msg_length=len(original_msg),
                                 probability_table=AE.probability_table)

decoded_msg = "".join(decoded_msg)
with open("output.txt", "w") as l:
        l.write(decoded_msg)
