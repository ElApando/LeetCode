""" Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only
 once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

def delete_duplicates(ls_info: list) -> list:
    """ Eliminación de duplicados

    Parameters:
        - ls_info *(list)* - Lista con los datos de interés
    Returns:
        - ls_save *(list)* - Lista con los datos ordenados de menor a mayor sin duplicados
    """
    ls_save = []

    for jj in range(0,len(ls_info),1):
        if not ls_info[jj] in ls_save:
            ls_save.append(ls_info[jj])

    return ls_save.sort()

ls_data = [[1,1,2],[1,1,2,3,3],[1,2,3,6,5,4]]

for ii in range(0,len(ls_data),1):
    print(delete_duplicates(ls_data[ii]))

# Finite Incantatem
