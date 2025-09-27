""" 125 Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
 removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
 characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

import re

def isPalindrome(st_word: str) -> bool:
    """
    """
    st_clean = re.sub(r"[^\w\s]|_","",st_word).replace(" ","").lower()
    print(st_clean)
    st_check = st_clean[::-1]

    return st_check == st_clean


ls_prove = ["A man, a plan, a canal: Panama", "race a car", " ", "ab_a"]

ls_test = [isPalindrome(ii) for ii in ls_prove]

print(ls_test)

# Finite Incantatem
