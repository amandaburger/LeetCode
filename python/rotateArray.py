def rotate(nums, k):
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums

nums1=[1,2]
k1=3
print(rotate(nums1,k1))
nums2=[-1,-100,3,99]
k2=2