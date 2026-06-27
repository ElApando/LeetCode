""" Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climb_stairs( in_n: int) -> int:
    """ climb_stairs

    Parameters:
        - in_n *(int)* - Número de pasos
    Returns:
        -  ls_save *(list)* - Pasos finales 
    """
    ls_save = [0] * (in_n + 1); ls_save[0] = 1; ls_save[1] = 1

    for i in range(1, in_n + 1,1):
        ls_save[i] = ls_save[i-1] + ls_save[i-2]
    
    return ls_save[-1]

ls_exercise = [2,3]

for i in range(0,len(ls_exercise),1):
    print(climb_stairs(ls_exercise[i]))

# Finite Incantatem