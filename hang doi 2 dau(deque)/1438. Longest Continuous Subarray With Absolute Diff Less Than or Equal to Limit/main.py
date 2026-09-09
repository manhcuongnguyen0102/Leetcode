from collections import deque
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_qp = deque()
        min_qp = deque()
        left = 0
        max_qp_len = 0
        for right in range(len(nums)):
            while max_qp and max_qp[-1]<nums[right]:
                max_qp.pop()
            while min_qp and min_qp[-1] > nums[right]:
                min_qp.pop()
            max_qp.append(nums[right])
            min_qp.append(nums[right]) 
            while max_qp[0] - min_qp[0] > limit:
                if max_qp[0] == nums[left]:
                    max_qp.popleft()
                if min_qp[0] ==nums[left]:
                    min_qp.popleft()
                left+=1
            max_qp_len = max(max_qp_len,right-left+1)
            
        return max_qp_len