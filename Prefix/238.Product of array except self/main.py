class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        rel = [0]*(len(nums))
        left_pro =[1]*(len(nums)+1)
        right_pro = [1]*(len(nums)+1)
        n = len(nums)
        for i in range(n):
            left_pro[i+1] = nums[i]*left_pro[i]
            right_pro[i+1] = nums[n-i-1]*right_pro[i]
        for i in range(n):
            rel[i] = left_pro[i]*right_pro[n-i-1]
        return rel