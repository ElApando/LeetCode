def removeDuplicates(nums: list) -> int:

	Guarda = []

	for i in range(0,len(nums),1):
		if nums[i] in Guarda:
			pass

		else:
			Guarda.append(nums[i])

	Cantidad = len(Guarda)

	return Cantidad

Lista = [[1,1,2],[0,0,1,1,1,2,2,3,3,4]]

for i in range(0,len(Lista),1):
	Activo = removeDuplicates(Lista[i])
	print(Activo)