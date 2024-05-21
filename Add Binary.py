def addBinary(a: str, b: str) -> str:
    # print(int(a, 2),int(b, 2))
    # print(bin(int(a, 2)+ int(b, 2)))
    # print(bin(int(a, 2)+ int(b, 2))[2:])
    # print(str(bin(int(a, 2)+ int(b, 2)))[2:])

    # return 

    Guarda = []
    Conteo = 0
    i = len(a) - 1;  j = len(b) - 1

    while i >= 0 or j >= 0 or Conteo:
      if i >= 0:
        Conteo += int(a[i])
        i -= 1
      if j >= 0:
        Conteo += int(b[j])
        j -= 1
      Guarda.append(str(Conteo % 2))
      Conteo //= 2

    Cadena = "".join(Guarda[::-1])

    return Cadena

a = ["11","1010"]
b = ["1","1011"]

for i in range(0,len(a),1):
    Activo = addBinary(a[i],b[i])
    print(Activo)