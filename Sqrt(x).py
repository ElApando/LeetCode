import math as m

def mySqrt(x: int) -> int:

    Numero = int(m.sqrt(x))

    return Numero

a = [4,8]

for i in range(0,len(a),1):
    Activo = mySqrt(a[i])
    print(Activo)