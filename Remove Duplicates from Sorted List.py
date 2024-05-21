def deleteDuplicates(head: list) -> list:
    
    Lista = head
    Guarda = []

    for i in range(0,len(Lista),1):
        if Lista[i] in Guarda:
            pass

        else:
            Guarda.append(Lista[i])

    Guarda.sort()

    return Guarda

a = [[1,1,2],[1,1,2,3,3],[1,2,3,6,5,4]]

for i in range(0,len(a),1):
    Activo = deleteDuplicates(a[i])
    print(Activo)