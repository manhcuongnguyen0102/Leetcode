class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k==0:
            return False
        window = set()
        for index,value in enumerate(nums):
            if value in window:
                return True
            window.add(value)
            if len(window)>k:
                window.remove(nums[index-k])
                
        return False   
        