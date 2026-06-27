""" Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two 
integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the 
array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote 
the elements that should be merged, and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.


Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge 
result can fit in nums1.
"""

def merge(ls_num_1: list, in_m: int, ls_num_2: list, in_n: int) -> None:
    """convierte dos listas en una medianteun merge artesanal

    Parameters:
        - ls_num_1 *(list)* -Lista con los primeros datos
        - in_m *(int)* - Tamaño de la primera lista sin contar los ceros
        - ls_num_2 *(list)* -  Lista con los segundos datos
        - in_n *(int)* - Tamaño de la lista sin contar los ceros
    Returs:
        - ls_num_1 *(list)* - Lista con el contenido de ambas listas  
    """

    if in_n == 0:
        return

    if in_n == 1 and len(ls_num_1) == 1:
        ls_num_1[0] = ls_num_2[0]

    else:
        for jj in range(0,in_n,1):
            ls_num_1[jj-in_n] = ls_num_2[jj]

    ls_num_1.sort()

    return ls_num_1

a = [[1,2,3,0,0,0],[1],[0],[0,0,0,0,0],[1,0]]
b = [3,1,0,0,1]
c = [[2,5,6],[],[1],[1,2,3,4,5],[2]]
d = [3,0,1,5,1]

for ii in range(0,len(a),1):
    print(merge(a[ii],b[ii],c[ii],d[ii]))

# Finite Incantatem
