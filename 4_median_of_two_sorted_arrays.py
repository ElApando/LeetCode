""" Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the 
median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
"""

def find_median_sorted_arrays(ls_num_1:list, ls_num_2:list)->float:
    """ La función encuentra la media de las listas ingresadas
    Parameters:
        - ls_num_1 *(list)* - Lista con datos de tipo entero
        - ls_num_2 *(list)* - Lista con datos de tipo entero
    Returns:
        - fl_median *(float)* - Valor medio de la suma de las dos listas 
    """

    for jj in ls_num_2:
        ls_num_1.append(jj)

    ls_num_1.sort()
    in_lenght = len(ls_num_1)
    in_half = int(in_lenght/2)

    if in_lenght % 2 == 0:
        in_num_1 = ls_num_1[in_half-1]
        in_num_2 = ls_num_1[in_half]
        fl_median = (float(in_num_1) + float(in_num_2))/2

    else:
        fl_median = ls_num_1[in_half]

    return float(fl_median)

ls_data = [[[1,3],[2]],[[1,2],[3,4]],[[],[2,3]]]

for ii in ls_data:
    print(find_median_sorted_arrays(ii[0],ii[1]))

# Finite Incantatem
