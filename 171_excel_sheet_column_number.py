""" 171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701
"""

from typing import Dict, List

di_refs: Dict[str, int] = { "A": 1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9,
    "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20,
    "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}

ls_prove: List[int] = [1, 28, 701, 2147483647]

def convert_to_title(column_number: int) -> str:
    """El código obtiene las columnas de Excel, solo se debe de ingresar el índice requerido
    se debe de ir dividiendo entre 26 dado que es la cantidad de lentras en el abecedario, hasta 
    que el resuido sea cero"""
    result = ""
    if column_number in di_refs:
        result = di_refs[column_number]

    else:
        while column_number > 0:
            minus_num = column_number - 1
            num_num = 1 + (minus_num) % 26
            result = di_refs[num_num] + result
            column_number = minus_num//26

    return result


for prove in ls_prove:
    print(convert_to_title(prove))

# Finite Incantatem
