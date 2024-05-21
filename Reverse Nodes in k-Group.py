def findMedianSortedArrays(k, Lista):

    Lista_General = []
    Tamaño = int(len(Lista)/k)
    Conteo = 0
    Acumulado = k

    for i in range(Tamaño):
        Objetivo = Lista[i*k:Acumulado]
        Objetivo.reverse()
        Lista_General.append(Objetivo)
        Acumulado = Acumulado + k

    Lista_General.append(Lista[Acumulado-k:])
    Lista_Final = []

    for i in range(len(Lista_General)):
        for j in range(0,len(Lista_General[i]),1):
            Lista_Final.append(Lista_General[i][j])

    return Lista_Final

Lista = [[1,2,3,4,5], [1,2,3,4,5]]; k = [2,3]

for i in range(0,len(Lista),1):
    Activo = findMedianSortedArrays(k[i],Lista[i])
    print("WWW",Activo)
