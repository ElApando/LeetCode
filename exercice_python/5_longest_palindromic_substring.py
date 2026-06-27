""" Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

def longest_palindrome(st_word: str) -> str:
    """ longest_palindrome
    
    Parameters:
		- st_word *(str)* - Palabra que contine el paindromo
    Returns:
		- ls_save *(list)* - Palindromo
    """
    ls_save = []
    st_check = ""
    in_flag = 0

    if len(st_word) == 1:
        return st_word

    for _ in range(0,len(st_word),1):
        for jj in range(0,len(st_word[in_flag:]),1):
            st_check = st_check + st_word[jj+in_flag]

            if st_check == st_check[::-1]:
                ls_save.append(st_check)

                if len(st_check) == len(st_word[in_flag:]):
                    in_max = 0
                    st_word_length = ""

                    for element in ls_save:
                        size = len(element)

                        if size > in_max:
                            st_word_length = element
                            in_max = size

                    ls_save = st_word_length

                    if ls_save == "":
                        ls_save = st_word[0]

                    return ls_save

            elif len(st_check) == len(st_word[in_flag:]):
                in_flag = in_flag+1
                st_check = ""

    return ls_save

ls_prove = ["babad","cbbd","bb","qweewq","a","ac","abb","abadd","babadada"]#["cbcdcbedcbc"]#

for ii in range(0,len(ls_prove),1):
    print(longest_palindrome(ls_prove[ii]))

# Finite Incantatem
