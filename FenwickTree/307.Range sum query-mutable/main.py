class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.n = len(nums)
        self.bit = [0]*(self.n+1)
        for i in range(self.n):
            self.add(i+1,nums[i])
    def add(self,post,val):
        while post <=self.n:
            self.bit[post]+=val
            post+=post&(-post)

    def update(self, index: int, val: int) -> None:
        
        delta = val-self.nums[index]
        self.nums[index] = val
        self.add(index+1,delta)
    def query(self, post):
        sum = 0
        while post > 0:
            sum+= self.bit[post]
            post -= post &(-post)
        return sum
    def sumRange(self, left: int, right: int) -> int:
        return self.query(right+1)-self.query(left)


