def mergeTwoLists(list1: list, list2: list) -> list:

	Guarda = []

	Guarda = list1+list2
	Guarda.sort()

	return Guarda

Lista = [[1,2,4],[1,3,4]]
Activo = mergeTwoLists(Lista[0],Lista[1])
print(Activo)