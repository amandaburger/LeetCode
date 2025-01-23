def twoSum(self, nums: List[int], target: int) -> List[int]:
    mapp = {}
    for i in range(len(nums)):
        amountLeft = target-nums[i]
        if amountLeft in mapp:
            return [mapp[amountLeft], i]
        mapp[nums[i]]= i
    return[]

nums = [2,7,11,15]
target = 9

nums2 = [3,3]
target2 = 6
print(twoSum(nums, target))
print(twoSum(nums2,target2))