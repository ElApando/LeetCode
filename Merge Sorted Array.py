def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    # m = m - 1
    if n == 0:
        return

    if n == 1 and len(nums1) == 1:
        nums1[0] = nums2[0]

    else:
        for i in range(0,n,1):
            print(nums1[i-n],nums2[i],i)
            nums1[i-n] = nums2[i]

    nums1.sort()

    return nums1

a = [[1,2,3,0,0,0],[1],[0],[0,0,0,0,0],[1,0]]
b = [3,1,0,0,1]
c = [[2,5,6],[],[1],[1,2,3,4,5],[2]]
d = [3,0,1,5,1]

for i in range(0,len(a),1):
    print(a[i],b[i],c[i],d[i])
    Activo = merge(a[i],b[i],c[i],d[i])
    print(Activo)