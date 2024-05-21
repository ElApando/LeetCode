def plusOne(digits: list) -> list:

    Numeros = digits
    Guarda_Numero = ""

    for i in range(0,len(Numeros),1):
        Guarda_Numero = Guarda_Numero + str(Numeros[i])

    Operacion = str(int(Guarda_Numero) + 1)
    
    Guarda_Lista = []
    for i in Operacion:
        Guarda_Lista.append(int(i))

    return Guarda_Lista

Palabra = [[1,2,3],[4,3,2,1],[9]]

for i in range(0,len(Palabra),1):
    Activo = plusOne(Palabra[i])
    print(Activo)

