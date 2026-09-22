class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        current_sum = 0
        rel = 0
        fre = {0:1}
        for i in range(len(nums)):
            current_sum+= nums[i]
            target = current_sum - k
            if target in fre:
                rel += fre[target]
            if current_sum in fre:
                fre[current_sum]+=1
            else:
                fre[current_sum]=1
        return rel
