"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

"""

from typing import List

def get_row(row_index: int) -> List[int]:
    """ Genera el triángulo de pascal

    Parameters:
        - row_index *(int)* -  índice del renglon que se requiere

    Returns
        - ls_save *(List)* - Lista con el renglon correspondiente
    """

    ls_save = []
    ls_keept = [1,1]

    for ii in range(0,row_index+1,1):
        if ii == 0:
            ls_save.append([1])

        elif ii == 1:
            ls_save.append([1,1])

        else:
            ls_keept = ls_save[1].copy()

            for jj in range(1,len(ls_save[ii-1]),1):
                in_sum = ls_save[ii-1][jj-1] + ls_save[ii-1][jj]
                ls_keept.insert(jj,in_sum)

            ls_save.append(ls_keept)

    return ls_save[row_index]

# Finite Incantatem
