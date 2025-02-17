import heapq

def findKthLargest(nums,k):
    heap = nums[:k]
    print(heap)
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    return heap[0]
print(findKthLargest([3,2,1,5,6,4],2))
print(findKthLargest([3,2,3,1,2,4,5,5,6],4))
