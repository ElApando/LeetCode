"""Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore 
it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
"""

def solution(in_x: int) -> bool:
    """ Buca palindromos en nummeros
    
    Parameters:
		- in_x *(int)* - Número que será evluado
    Returns:
		- conditional *(bool)* - Resulado de la evaluación
    """

    st_x = str(in_x)
    st_y = str(st_x[::-1])

    return st_x == st_y

prove = [121,-121,10]

for ii in range(0,len(prove),1):
    print(solution(prove[ii]))

# Finite Incantatem
