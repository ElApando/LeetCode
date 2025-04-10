""" Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""

def add_binary(st_a: str, st_b: str) -> str: 
    """add_binary

    Toma 2 cadenas de textos binarias y retorna la suma

    Parameters:
      - st_a (str) - 
      - st_b (str) - 
    Returns:
      - st_string (str) -
    """

    ls_save = []
    in_count = 0
    ii = len(st_a) - 1;  jj = len(st_b) - 1

    while ii >= 0 or jj >= 0 or in_count:
      if ii >= 0:
        in_count += int(st_a[ii])
        ii -= 1
      if jj >= 0:
        in_count += int(st_b[jj])
        jj -= 1
      ls_save.append(str(in_count % 2))
      in_count //= 2

    st_string = "".join(ls_save[::-1])

    return st_string

a = ["11","1010"]
b = ["1","1011"]

for ii in range(0,len(a),1):
    st_active = add_binary(a[ii],b[ii])
    print(st_active)

# Finite Incantatem
