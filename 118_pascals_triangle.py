"""118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""
from typing import List

def generate(num_rows:int) -> List[List[int]]:
    """ Gnera el triángulo de pascal

    Parameters:
        - num_rows *(int)* -  Número de renglones que tendra el triángulo

    Returns
        - ls_save *(List)* - Lista con los números correspondientes
    """

    ls_save = []
    ls_keept = [1,1]

    if num_rows == 0:
        return []

    for ii in range(0,num_rows,1):
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

    return ls_save


ls_prove = [0,1,2,3,4,5,6,7]
for element in ls_prove:
    print(generate(element))

# Finite Incantatem
