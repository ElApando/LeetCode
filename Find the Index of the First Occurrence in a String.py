def searchInsert(nums: list, target: int) -> int:
	if target in nums:
		for i in range(0,len(nums),1):
			if nums[i] == target:
				return i

	else:
		nums.append(target)
		nums.sort()
		for i in range(0,len(nums),1):
			if nums[i] == target:
				return i


Lista = [[1,3,5,6],[1,3,5,6],[1,3,5,6]]; Palabra = [5,2,7]

for i in range(0,len(Lista),1):
	Activo = searchInsert(Lista[i],Palabra[i])
	print(Activo)
