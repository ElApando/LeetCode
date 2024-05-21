def removeElement(nums: list, val: int) -> int:

    Guarda = []

    for i in range(0,len(nums),1):
        if nums[i] == val:
            pass

        else:
            Guarda.append(nums[i])

    Cantidad = len(Guarda)

    return Cantidad

Lista = [[3,2,2,3],[0,1,2,2,3,0,4,2]]; Numeros = [3,2]

for i in range(0,len(Lista),1):
    Activo = removeElement(Lista[i],Numeros[i])
    print(Activo)