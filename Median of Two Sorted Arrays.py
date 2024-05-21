
def findMedianSortedArrays(nums1, nums2):

    for i in nums2:
        nums1.append(i)

    nums1.sort()
    Tamano = len(nums1)
    Mitad = int(Tamano/2)

    if Tamano % 2 == 0:
        Numero1 = nums1[Mitad-1]
        Numero2 = nums1[Mitad]
        Mediana = (float(Numero1) + float(Numero2))/2

    else:
        Mediana = nums1[Mitad]

    return float(Mediana)

Lista = [[[1,3],[2]],[[1,2],[3,4]],[[],[2,3]]]

for elemento in Lista:
 
    Activo = findMedianSortedArrays(elemento[0],elemento[1])
    print("WWW",Activo)