"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified
 list.
k is a positive integer and is less than or equal to the length of the linked list. If the number
 of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""

def find_median_sorted_arrays(in_k:int, ls_data:list):
    """ Encuentra el valor medio de una lista

    Parameters:
        - 
    Returns:
        - 
    """

    ls_save = []
    in_lenght = int(len(ls_data)/in_k)
    in_accumulate = in_k

    for jj in range(in_lenght):
        ls_goal = ls_data[jj*in_k:in_accumulate]
        ls_goal.reverse()
        ls_save.append(ls_goal)
        in_accumulate = in_accumulate + in_k

    ls_save.append(ls_data[in_accumulate-in_k:])
    ls_keep = []

    for jj in range(0,len(ls_save),1):
        for kk in range(0,len(ls_save[jj]),1):
            ls_keep.append(ls_save[jj][kk])

    return ls_keep

ls_prove = [[1,2,3,4,5], [1,2,3,4,5]]
ls_k = [2,3]

for ii in range(0,len(ls_prove),1):
    print(find_median_sorted_arrays(ls_k[ii],ls_prove[ii]))

# Finite Incantatem
