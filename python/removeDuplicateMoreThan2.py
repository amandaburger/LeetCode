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

def removeDuplicates2(nums) -> int:
    if len(nums) == 1:
        return 1
    i, j = 2, 2
    for i in range(2,len(nums)):
        if nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1
    return j

nums1 = [1,1,1,2,2,3]
nums2=[0,0,1,1,1,1,2,3,3]

print("first way")
print( removeDuplicates(nums1), nums1)

print( removeDuplicates(nums2), nums2)      

print("Second way")

print( removeDuplicates2(nums1), nums1)

print( removeDuplicates2(nums2), nums2)  