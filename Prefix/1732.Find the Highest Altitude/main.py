class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix = [0]*(len(gain)+1)
        premax = 0
        for i in range(1,len(gain)+1):
            prefix[i]= prefix[i-1]+gain[i-1]
            if premax < prefix[i]:
                premax = prefix[i]
        return premax