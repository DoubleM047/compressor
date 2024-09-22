from decimal import getcontext, Decimal
import struct
import decoderV2

getcontext().prec = 200000

slovar = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\n']


x = open("input.txt", "r").readlines()
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
        b = Decimal(interval[0])
        multiplier = Decimal(interval[1])-Decimal(interval[0])
        interval.clear()
        interval.append(Decimal(slovar.index(l))*Decimal(0.01)*multiplier+b)
        interval.append(Decimal(slovar.index(l)+1)*Decimal(0.01)*multiplier+b)



counter = 0
for i in x:
     counter += len(i)

#print(interval[0])

rezultat = decoderV2.decode(interval[0], slovar, counter)

with open("output.txt", "w") as l:
        l.write(rezultat)

bytes = struct.pack("d", interval[0])
with open("binary.bin", "wb") as f:
    f.write(bytes)
