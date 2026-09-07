class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        cnt_0 = 0
        cnt_1 = 0
        for i in students:
            if i == 0:
                cnt_0+=1
            else :
                cnt_1+=1
        for i in sandwiches:
            if i == 1:
                if cnt_1 == 0:
                    break
                cnt_1-=1
            else: 
                if cnt_0 == 0:
                    break
                cnt_0-=1
        return cnt_1+cnt_0
            
            