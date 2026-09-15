class NumArray:

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.nums = nums
        # set up memory for treeSeg
        self.t = [0]*(4*self.n)
        if self.n > 0:
            self.built(0,0,self.n -1)
    def built(self, v,l,r):
        if(l == r):
            self.t[v] = self.nums[l]
        else:
            mid = (l+r)//2
            self.built(2*v+1,l,mid)
            self.built(2*v+2,mid+1,r)
            self.t[v] = self.t[2*v+1]+ self.t[2*v+2]
    def query(self,v,tl,tr,l,r):
        if(l>r): return 0
        if(tl == l and tr == r):
            return self.t[v] 
        else:
            tmid = (tl+tr)//2
            s1 = self.query(2*v+1, tl,tmid,l,min(r,tmid))
            s2 = self.query(2*v+2,tmid+1, tr,max(tmid+1,l),r)
            return s1+s2
    def sumRange(self, left: int, right: int) -> int:
        return self.query(0,0,self.n-1,left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)