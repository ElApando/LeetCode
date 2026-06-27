""" Longest Subsrting Withouth Repeating

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def solution(st_word: str) -> int:
    """ enccuenntra las letras sin duplicados
    
    Parameters:
		- st_word *(str)* - Palabra que será evaluada
    Returns:
		- in_length *(int)* - Conteo de las letras sin repeticiones
    """

    st_save = ""
    in_length, in_count = 0,0
    di_save = {}

    while in_count < len(st_word):
        st_character = st_word[in_count]
        if st_character not in di_save:
            di_save[st_character] = in_count
        else:
            if di_save[st_character]+ 1 > in_length:
                in_length = di_save[st_character]+1
            di_save[st_character] = in_count

        if len(st_save) < in_count-in_length+1:
            st_save = st_word[in_length:in_count+1]

        in_count += 1

    if len(st_save) < in_count-in_length:
        st_save = st_word[in_length:in_count]

    return len(st_save)

Prueba = ["AbcabCBB","BBBBB","PWWKEW"]

for ii in range(0,len(Prueba),1):
    print(solution(Prueba[ii]))

# Finite Incantatem
