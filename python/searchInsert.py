def searchInsert(nums,target):
    for index, value in enumerate(nums):
        if value >= target:
            return index
    return len(nums)
print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))
print(searchInsert([1,3,5,6],0))
