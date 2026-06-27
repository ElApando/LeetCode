""" Merge k sorted
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

def merge_k_lists(ls_object:list)->list:
    """ Une y ordena la lista o las listas de  menor a mayor

    Parameters:
        - ls_object *(list)* - Lista con la información correspondiente
    Returns:
        - ls_save *(list)* - Lista con ell resultado correspndiente ordenado de menor a mayor
    """

    ls_save = []

    for ii in ls_object:
        for jj in ii:
            ls_save.append(jj)

    ls_save.sort()

    return ls_save

ls_data = [[1,4,5],[1,3,4],[2,6]]
print(merge_k_lists(ls_data))

# Finite Incantatem
