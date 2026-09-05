class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for index,value in enumerate(nums):
            take = target - value
            if take in seen:
                return [seen[take],index]
            
            seen[value] = index 
        return []       
        
        