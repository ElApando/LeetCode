""" Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers 
and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

def solution(ls_work_1:list, ls_work_2:list) -> list:
    """ Suma de dos números
    
    Parameters:
		- ls_work_1 *(list)* - Primer número de la suma
        - ls_work_2 *(list)* - Segundo número de la suma
    Returns:
		- ls_save *(list)* - Lista con el resultado correspondiente
    """

    ls_save = []
    in_save = 0

    while ls_work_1 or ls_work_2 or in_save:
        ls_num_1 = ls_work_1.pop() if ls_work_1 else 0
        ls_num_2 = ls_work_2.pop() if ls_work_2 else 0
        in_sum = ls_num_1 + ls_num_2 + in_save
        in_save = in_sum // 10
        ls_save.append(in_sum % 10)

    return ls_save

ls_data_1 = [[2,4,3],[0],[9,9,9,9,9,9,9]]
ls_data_2 = [[5,6,4],[1],[9,9,9,9]]

for ii in range(0,len(ls_data_1),1):
    print(solution(ls_data_1[ii], ls_data_2[ii]))

# Finite Incantatem
