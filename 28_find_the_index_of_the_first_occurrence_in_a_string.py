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

def str_str(st_haystack:str, st_needle:str)->int:
    """ Busca la palabra dentro de la palabra

    Parameters:
        - st_haystack *(str)* - Palabra en la que se busca
        - st_needle *(str)* - Palabra que se busca 
    Returns:
        - result *(int)* - Es la ubicación de la busqueda, en caso de no contener la palabra
            retorna -1
    """

    if len(st_haystack) != 1:
        for jj in range(0,len(st_haystack)-len(st_needle)+1,1):
            print(st_haystack[jj:jj+len(st_needle)])
            if st_haystack[jj:jj+len(st_needle)]==st_needle:
                return jj

    else:
        if st_haystack == st_needle:
            return 0


    return -1

ls_haystack_data = ["sadbutsad","leetcode","mississippi","mississippi", "a", "abc"]
ls_needle_data = ["sad","leeto","issi","issip", "a", "c"]

for ii in range(0,len(ls_needle_data),1):
    print(str_str(ls_haystack_data[ii], ls_needle_data[ii]))

# Finite Incantatem
