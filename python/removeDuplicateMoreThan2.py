def removeDuplicates(nums) -> int:
        index = 1
        occurance = 1
        for i in range(1, len(nums)):
            if nums[i]== nums[i-1]:
                occurance +=1
            else:
                occurance = 1
            
            if occurance <=2:
                nums[index]=nums[i]
                index+=1
        return index

nums1 = [1,1,1,2,2,3]
nums2=[0,0,1,1,1,1,2,3,3]

print( removeDuplicates(nums1), nums1)

print( removeDuplicates(nums2), nums2)               