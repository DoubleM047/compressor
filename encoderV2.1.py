from decimal import getcontext, Decimal
import decimal
import struct
import decoderV2



slovar = [' ', '!', '\n', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']


x = open("input.txt", "r").readlines()

counter = 0
for i in x:
     counter += len(i)

print(counter)
getcontext().prec = 2*counter

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

def decimal_to_binary_float(dec):
    integer_part = int(dec)
    fractional_part = dec - integer_part

    binary_integer = bin(integer_part).lstrip('0b') or '0'
    

    binary_fraction = []
    while fractional_part != 0 and len(binary_fraction) < 16: 
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fraction.append(str(bit))
        fractional_part -= bit
    
    return f'{binary_integer}.' + ''.join(binary_fraction) if binary_fraction else binary_integer

dec_float = decimal.Decimal('42.625')


binary_representation = decimal_to_binary_float(dec_float)

with open("output.bin", "wb") as binary_file:

    binary_file.write(binary_representation.encode('utf-8'))
really_long_float = interval[0]
podpis, stevke, eksponent = really_long_float.as_tuple()
mantisa = int(''.join(map(str, stevke)))

with open("file.bin", "wb") as f:
    f.write(struct.pack('B', podpis)) 
    f.write(mantisa.to_bytes((mantisa.bit_length() + 7) // 8, 'big'))
    f.write(eksponent.to_bytes(4, 'big', signed=True))

with open("file.bin", "rb") as f:
    podpis = struct.unpack('B', f.read(1))[0]
    mantisa_bytes = f.read()[:-4] 
    eksponent = int.from_bytes(f.read(4), 'big', signed=True)  
    mantisa = int.from_bytes(mantisa_bytes, 'big')  


mantisa = str(mantisa)
mantisa = "0."+mantisa
really_long_float_from_file = Decimal(mantisa)

rezultat = decoderV2.decode(really_long_float_from_file, slovar, counter)

rezultat = decoderV2.decode(interval[0], slovar, counter)

with open("output.txt", "w") as l:
        l.write(rezultat)

