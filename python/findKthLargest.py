import heapq

def findKthLargest(k,nums):
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
        print(heap)
    return heap[0]
print(findKthLargest([3,2,1,5,6,4],2))
print(findKthLargest([3,2,3,1,2,4,5,5,6],4))
