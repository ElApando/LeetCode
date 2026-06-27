""" 7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
 the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

def reverse(x: int) -> int:
    """ Reversa 

    La función voltea el digito y comprueba que solo utilice 32-bit

    Parameters:
        - x *(int)* - Valor al que se le invertira la secuencia
    Returns:
        - x *(int)* - Con la secuencia invertida
    """

    x = str(x)
    x = x[::-1]

    if "-" in x:
        x = x.replace("-","")
        x = "-" + x

    x = int(x)

    if x <= (-2**31) or x >= ((2**31)-1):
        x = 0

    return x

ls_prove = [123, -123, 120]

for prove in ls_prove:
    print(reverse(prove))

# Finite Incantatem
