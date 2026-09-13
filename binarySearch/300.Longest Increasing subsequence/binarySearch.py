class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = []
        for x in nums:
            left = 0
            right = len(sub)-1
            while left<=right:
                mid = (left+right)//2
                if x > sub[mid]:
                    left = mid+1
                elif x <= sub[mid]:
                    right = mid-1
            if left == len(sub):
                sub.append(x)
            else:
                sub[left] = x
        return len(sub)
                    
                    
