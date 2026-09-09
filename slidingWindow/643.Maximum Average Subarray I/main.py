class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current = sum(nums[:k])
        max_out = current
        for i in range(k,len(nums)):
            current = current + nums[i]- nums[i]
            if current > max_out:
                max_out = current
        return max_out/k
        
            
            