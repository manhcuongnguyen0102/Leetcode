class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dup = {}
        for index,value in enumerate(nums):
            if value in dup:
                if abs(dup[value]-index) <= k:
                    return True            
            dup[value]=index 
        return False   
        