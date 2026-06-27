"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
"""

def solution(st_word:str) -> str:
    """ Da las letras repetidos
    
    Parameters:
	    - st_word *(str)* - Palabra de interés
    Returns:
        - st_result *(str)* - Letras en común en las palabras
    """

    st_result = ""
    st_order = sorted(st_word)
    st_first = st_order[0]
    st_last = st_order[-1]


    for jj in range(min(len(st_first),len(st_last))):
        if st_first[jj] != st_last[jj]:
            return st_result

        st_result += st_first[jj]

    return st_result

ls_prove = [["flower","flow","floght","flight","fly"],["dog","racecar","car"],
            ["war","warm","warning"]]

for ii in range(0,len(ls_prove),1):
    print(solution(ls_prove[ii]))

# Finite Incantatem
