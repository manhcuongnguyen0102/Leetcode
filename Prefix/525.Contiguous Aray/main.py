class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        current_sum = 0 
        fre = {0:-1}
        max_len =0
        for i in range(n):
            if nums[i] == 1:
                current_sum +=1
            else:
                current_sum -=1
            if current_sum not in fre:
                fre[current_sum]=i
            else:
                cur_len = i- fre[current_sum]
                if max_len< cur_len:
                    max_len = cur_len
        return max_len
                
                
            