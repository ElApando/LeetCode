""" Trappinng  Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

def solution(ls_data: list) -> int:
    """ Agua atapada en el relieve
    
    Parameters:
		- ls_data *(list)* - Lista con el relieve 
    Returns:
		- in_result *(int)* 
    
    """
    ls_left = []
    ls_right = []
    in_result = 0
    in_left_max = 0
    in_right_max = 0

    for jj in range(0,len(ls_data),1):
        if jj == 0:
            ls_left.append(0)
            in_left_max = max(in_left_max, ls_data[jj])

        else:
            ls_left.append(in_left_max)
            in_left_max = max(in_left_max, ls_data[jj])

    ls_reverse = ls_data[::-1]

    for i in range(0,len(ls_reverse),1):
        if i == len(ls_reverse)-1:
            ls_right.append(0)
            in_right_max = max(in_right_max, ls_reverse[i])

        else:
            ls_right.append(in_right_max)
            in_right_max = max(in_right_max, ls_reverse[i])

    ls_right = ls_right[::-1]

    for jj in range(0, len(ls_left), 1):
        in_value = min(ls_left[jj], ls_right[jj]) - ls_data[jj]

        if in_value > 0:
            in_result += in_value

    return in_result

ls_prove = [[0,1,0,2,1,0,1,3,2,1,2,1],[0,1,5,2,0,1,3,2,1,4],[4,2,0,3,2,5]]

for ii in range(0,len(ls_prove),1):
    print(solution(ls_prove[ii]))

# Finite Incantatem
