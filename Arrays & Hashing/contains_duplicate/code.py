"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true


Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

"""

def containsDuplicate(nums):
    numsSet = set()
    for i in nums:
        if i in numsSet:
            return True
        numsSet.add(i)
    return False

print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 7, 9, 10]))