from decimal import getcontext, Decimal
getcontext().prec = 1000000000000


def rez(interval):
    temp=[]
    temp.append(interval[-3])
    temp.append(interval[-2])
    interval.clear()
    interval.append(temp[0])
    interval.append(temp[-1])

    return interval

def decode(message:float, slovar:dict, dol:int):

    getcontext().prec = 10000000000000000

    rezultat = ""
    interval = [0, 1]


    for i in range(dol):
        for j in slovar:
            interval.insert(-1, Decimal(interval[-1]-interval[0])*Decimal(slovar[j])+interval[-2])
            if interval[-2] > message:
                    rezultat += j
                    break
        interval = rez(interval)

    return rezultat


