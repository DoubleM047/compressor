from decimal import getcontext, Decimal
import struct
import decoder

getcontext().prec = 100000000

slovar = {
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
  "~": 0.01
}


x = open("input.txt", "r").readlines()
print(x)
interval = [0, 1]

def rez(interval):
    temp=[]
    temp.append(interval[-3])
    temp.append(interval[-2])
    interval.clear()
    interval.append(temp[0])
    interval.append(temp[-1])

    return interval


for i in x:
    for l in i:
        print(l)
        for j in slovar:
            interval.insert(-1, Decimal(interval[-1]-interval[0])*Decimal(slovar[j])+interval[-2])

            if j == i:
                break
        interval = rez(interval)

rezultat = decoder.decode(interval[0], slovar, len(x))

with open("output.txt", "w") as l:
        l.write(rezultat)

bytes = struct.pack("d", interval[0])
with open("binary.bin", "wb") as f:
    f.write(bytes)

