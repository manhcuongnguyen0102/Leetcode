class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        def find_0(target):
            left = 0
            right = len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]<target:
                    left = mid+1
                elif nums[mid]>=target:
                    right = mid-1
            return left
        neg_cnt = find_0(0)
        pos_cnt = len(nums)-find_0(1)
        return max(neg_cnt,pos_cnt)