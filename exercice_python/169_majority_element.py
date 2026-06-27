"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume
 that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

def majority_element(nums: list) -> int:
    """Extracción del elemento con mayor cantidad de repeticiones
    en la lista"""

    ls_unique = list(set(nums))
    di_save = {}
    for num in ls_unique:
        fl_num = nums.count(num)/2
        di_save[num] = fl_num
    in_max = max(di_save, key=di_save.get)
    return in_max

ls_prove = [[3,2,3],[2,2,1,1,1,2,2], [3,3,4]]

for prove in ls_prove:
    print(majorityElement(prove))

# Finite Incantatem
