class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        rel = [1]*(n)
        left_running = 1
        for i in range(n):
            rel[i] = left_running
            left_running*= nums[i]
        right_running = 1
        for i in range(n-1,-1,-1):
            rel[i]*=right_running
            right_running*= nums[i]
        return rel
            