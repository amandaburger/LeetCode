
from typing import List

def removeDuplicates(nums) -> int:
        if len(nums) == 1:
            return 1

        i = 0
        for j in range(1, len(nums)):
            if (nums[i] != nums[j]):
                i += 1
                nums[i] = nums[j]

        return i + 1

nums1= [0,0,0,1,1,1,2,3,3,3,4]
print(removeDuplicates(nums1))