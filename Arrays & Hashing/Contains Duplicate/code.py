def containsDuplicate(nums):
    numsSet = set()
    for i in nums:
        if i in numsSet:
            return True
        numsSet.add(i)
    return False

print('Please enter an array of numbers')



print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 7, 9, 10]))
