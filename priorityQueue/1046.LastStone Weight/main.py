import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x!=y:
                heapq.heappush(max_heap,(x-y))
        if max_heap:
            return max_heap[0]*-1
        else:
            return 0    
        
        
        