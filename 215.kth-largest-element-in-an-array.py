#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [0]

        for num in nums:
            heap.append(num)

        heapSize = len(heap)-1

        for i in range(heapSize, 1, -1):

            index = i
            while heap[index] > heap[index // 2] and index > 1:
                replace = heap[index // 2]
                heap[index // 2] = heap[index]
                heap[index] = replace
                index = index // 2

        for o in range(k):
            replace = heap[1]
            heap[1] = heap[heapSize]
            heap[heapSize] = replace
            heapSize-=1

            i = 1
            largest = 0
            while largest!=i:
                left = i*2 
                right = left+1   
                if left<=heapSize and heap[i]<heap[left]:
                    largest = left
                else:
                    largest = i
                
                if right<=heapSize and heap[right] > heap[largest]:
                    largest = right
                
                if i!=largest:
                    replace = heap[i]
                    heap[i] = heap[largest]
                    heap[largest] = replace
                    i = largest
                    largest = 0

        return heap[heapSize+1]


# @lc code=end
