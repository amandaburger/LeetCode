#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. 
#You may assume that the majority element always exists in the array.
def majorityElement(nums):
        count = 0
        curr = 0
        
        for num in nums:
            if count == 0:
                curr = num
            
            if num == curr:
                count += 1
            else:
                count -= 1
        
        return curr
nums1=[1,6,6,6,9]
nums2=[2,2,1,1,1,2,2]
print(majorityElement(nums1))