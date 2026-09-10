import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        fre = {}
        for i in nums:
            fre[i] = fre.get(i,0)+1
        min_heap = []
        for num,count in fre.items():
            heapq.heappush(min_heap,(count,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        rel = []
        for pair in min_heap:
            rel.append(pair[1])
        
        return rel
    