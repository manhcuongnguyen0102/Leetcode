class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.n = len(nums)
        self.t = [0]*(4*self.n)
        if self.n > 0:
            self.built(0,0,self.n-1)
    def built(self,v,left,right):
        if(left == right):
            self.t[v] = self.nums[left]
        else:
            mid  = (left+right)//2
            self.built(2*v+1,left,mid)
            self.built(2*v+2,mid+1,right)
            self.t[v] = self.t[2*v+1] + self.t[2*v+2]
    def _update(self,v,left,right, inx, val):
        if(left == right):
            self.t[v] = val
        else:
            mid = (left+right)//2
            if(inx <= mid):
                self._update(2*v+1,left,mid,inx,val)
            else:
                self._update(2*v+2,mid+1,right,inx,val)
            self.t[v] = self.t[2*v+1]+self.t[2*v+2]    
    def update(self, index: int, val: int) -> None:
        self._update(0,0,self.n-1,index,val)

    def query(self,v,tl,tr, left, right):
        if(left>right):
            return 0
        if(tl == left and tr == right):
            return self.t[v]
        else:
            tmid = (tl+tr)//2
            s1 = self.query(2*v+1,tl,tmid,left,min(tmid,right))
            s2 = self.query(2*v+2,tmid+1,tr,max(tmid+1,left),right)
            return s1+s2
    def sumRange(self, left: int, right: int) -> int:
        return self.query(0,0,self.n-1,left,right)


