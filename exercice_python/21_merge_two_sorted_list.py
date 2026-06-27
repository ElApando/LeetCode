"""  merge two sorted list

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the 
nodes of the first two lists.

Return the head of the merged linked list

Example 1
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

def merge_two_lists(ls_data_1: list, ls_data_2: list) -> list:
    """ Une dos listas y el resultado lo ordena de menor a mayor
    
    Parameters:
		- ls_data_1 *(list)* - Lista con datos principales
        - ls_data_2 *(list)* - Lista con datos secundarios
    Result:
		- ls_save *(list)* - Lista con la unión y ordenada de meenor a mayor
    
    """
    ls_save = ls_data_1+ls_data_2
    return ls_save.sort()

ls_data = [[1,2,4],[1,3,4]]
print(merge_two_lists(ls_data[0],ls_data[1]))

#Finite Incantatem
