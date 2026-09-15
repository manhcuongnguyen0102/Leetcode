class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        count = [0]*101
        for x in nums:
            count[x]+=1
        for i in range(1,101):
            count[i]+=count[i-1]
        rel = []
        for x in nums:
            if(x==0):
                rel.append(0)
            else:
                rel.append(count[x-1])
        return rel
                