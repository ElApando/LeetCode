""" Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such
 that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same
 element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

def two_sum(ls_data, ls_goal):
    """ Suma de dos números
    
    Parameters:
        - ls_data *(list)* - 
        - ls_goal *(list)* - 
    Returns:
	    - ls_
    
    """

    for jj in range(0,len(ls_data),1):
        for kk in range(0,len(ls_data),1):
            if ls_data[jj] == ls_data[kk]:
                if jj == kk:
                    pass

                else:
                    in_sum = ls_data[jj] + ls_data[kk]

                    if in_sum == ls_goal:
                        return [jj, kk]

            elif ls_data[jj] != ls_data[kk]:
                in_sum = ls_data[jj] + ls_data[kk]

                if in_sum == ls_goal:
                    return [jj, kk]

    return False

ls_prove = [[2,7,11,15],[3,2,4],[3,3]]
ls_nums = [9,6,6]

for i in range(0,len(ls_prove),1):
    print(two_sum(ls_prove[i],ls_nums[i]))

#  Finite Incantatem
