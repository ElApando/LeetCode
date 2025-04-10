""" Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

def length_of_last_word(st_word: str) -> int:
    """ Tamaño de la ultima palabra

    Parameters:
        - st_word *(str)* - Enuciado de interés
    Returns:
        - in_lenght *(int)* - Tamaño de la ultima palabra
    """
    st_split = st_word.split(" ")
    bo_flag = True

    while bo_flag:
        if st_split[-1] == "":
            st_split.pop(-1)
        elif st_split[-1] != "":
            bo_flag = False

    in_lenght = len(st_split[-1])

    return in_lenght

ls_word = ["Hello World","   fly me   to   the moon  ","luffy is still joyboy"]

for ii in range(0,len(ls_word),1):
    print(length_of_last_word(ls_word[ii]))

# Finite Incantatem
