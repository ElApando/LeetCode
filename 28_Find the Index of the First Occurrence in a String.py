""" Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle
 in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
"""
def search_insert(ls_nums: list, in_target: int) -> int:
    """Search Insert
    
    Parameters:
        - ls_nums *(list)* - Lista con los datos de interes
        - in_target *(int)* - Número objetivo
    Returns:
        - 
    """

    if in_target in ls_nums:
        for ii in range(0,len(ls_nums),1):
            if ls_nums[ii] == in_target:
                return ii

    else:
        ls_nums.append(in_target)
        ls_nums.sort()
        for ii in range(0,len(ls_nums),1):
            if ls_nums[ii] == in_target:
                return ii

ls_data = [[1,3,5,6],[1,3,5,6],[1,3,5,6]]
ls_target = [5,2,7]

for jj in range(0,len(ls_data),1):
    print(search_insert(ls_data[jj],ls_target[jj]))

# Finite Incantatem
