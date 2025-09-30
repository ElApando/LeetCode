"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

def single_number(nums: list[int]) -> int:
    """ Busqueda de un número único"""
    for num in nums:
        if nums.count(num) == 1:
            in_unique = num
            return in_unique

ls_prove = [[2,2,1], [4,1,2,1,2], [1]]

for prove in ls_prove:
    print(single_number(prove))

# Finite Incantatem
