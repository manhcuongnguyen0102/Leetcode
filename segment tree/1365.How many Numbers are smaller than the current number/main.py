class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        max_Val = 100
        tree = [0]*(4*(max_Val+1))
        def update(v, left,right,idx):
            if left == right:
                tree[v] +=1
                return
            else:
                mid = (left+right)//2
                if idx <= mid:
                    update(2*v+1,left, mid,idx)
                else:
                    update(2*v+2,mid+1,right,idx)
                tree[v] = tree[2*v+1]+ tree[2*v+2]
        def query(v, tl,tr,left,right):
            if(left > right):
                return 0
            if(tl ==  left and tr == right):
                return tree[v]
            else:
                tmid = (tl+tr)//2
                s1 = query(2*v+1,tl,tmid, left,min(tmid,right))
                s2 = query(2*v+2,tmid+1,tr,max(tmid+1,left),right)
                return s1+s2 
        for x in nums:
            update(0,0,max_Val,x)
        rel = []
        for i in nums:
            if(i==0):
                rel.append(0)
            else:
                fre = query(0,0,max_Val,0,i-1)
                rel.append(fre)
        return rel