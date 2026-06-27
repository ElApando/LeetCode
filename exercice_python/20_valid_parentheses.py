""" Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
 input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

"""

def solution(st_word: str) -> bool:
    """ Validación de parentesis
    
    """

    ls_save = []
    di_catalog = {")":"(","}":"{","]":"["}

    for jj in st_word:
        if jj in di_catalog.values():
            ls_save.append(jj)

        elif jj in di_catalog:
            if not ls_save or di_catalog[jj] != ls_save.pop():
                return False

        else:
            continue

    return not ls_save

prove = ["(}{)","()","()[]{}","(]","{[]}","(){}}{","(()(","({{{{}}}))"]

for ii in range(0,len(prove),1):
    print(solution(prove[ii]),prove[ii])

# Finite Incantatem
