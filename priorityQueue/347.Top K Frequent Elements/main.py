class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        fre = {}
        for i in nums:
            fre[i] = fre.get(i, 0) + 1
        sorted_fre = dict(sorted(fre.items(),key=lambda item:item[1],reverse=True))
        return list(sorted_fre.keys())[:k]
            
            