from decimal import getcontext, Decimal



def rez(interval):
    temp=[]
    temp.append(interval[-3])
    temp.append(interval[-2])
    interval.clear()
    interval.append(temp[0])
    interval.append(temp[-1])

    return interval

def decode(message:float, slovar:dict, dol:int):

    getcontext().prec = 2*dol

    rezultat = ""
    interval = [0, 1]
    

    for i in range(dol-1):
        lower = Decimal(interval[0])
        multiplier = (interval[1]-interval[0])
        interval.clear()
        a =  slovar[int((Decimal(message)-lower)//(Decimal(0.01)*multiplier))]
        interval.append(Decimal(slovar.index(a))*Decimal(0.01)*multiplier+lower)
        interval.append(Decimal(slovar.index(a)+1)*Decimal(0.01)*multiplier+lower)
        rezultat += a

    lower = Decimal(interval[0])
    multiplier = (interval[1]-interval[0])    
    a =  slovar[int((Decimal(message)-lower)//(Decimal(0.01)*multiplier))+1]

    return rezultat+a
