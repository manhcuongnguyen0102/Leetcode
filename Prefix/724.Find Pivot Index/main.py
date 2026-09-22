class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sumleft = [0]*(len(nums)+1)
        sumright = [0]*(len(nums)+1)
        n = len(nums)
        for i in range(n):
            sumleft[i+1] = sumleft[i]+nums[i]
            sumright[i+1]=sumright[i]+nums[n-i-1]
        for i in range(n):
            if sumleft[i] == sumright[n-i-1]:
                return i
            elif i==n-1:
                return -1

            