"""168. Excel Sheet Column Title
Given an integer column_number, return its corresponding column title as it appears in an Excel
 sheet.

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
Input: column_number = 1
Output: "A"

Example 2:
Input: column_number = 28
Output: "AB"

Example 3:
Input: column_number = 701
Output: "ZY"
 """

di_refs = { 1 :"A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J",
            11: "K", 12: "L", 13: "M", 14: "N", 15: "O",16: "P",17: "Q",18: "R",19: "S",20: "T",
            21: "U",22: "V",23: "W",24: "X",25: "Y",26: "Z"}

ls_prove = [1, 28, 701, 2147483647]

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
