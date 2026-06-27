""" Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
 The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer,
 2 is returned.
"""

import math as m

def my_sqrt(in_x: int) -> int:
    """ Obtiene la raíz cuadrada de un número

    Parameters:
        - in_x *(in_x)* - Número de interés
    Returns:
        - in_x *(in_x)* - Raíz cuadrada
    """
    return int(m.sqrt(in_x))

ls_prove = [4,8,16,111,1]

for i in range(0,len(ls_prove),1):
    print(my_sqrt(ls_prove[i]))

# Finite Incatatem
