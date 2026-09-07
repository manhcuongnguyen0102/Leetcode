from collections import deque
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        stu =deque()
        san = deque()
        for  _ in  students:
            stu.append(_)
        for  _ in sandwiches:
            san.append(_)
        is_run = True
        cnt_moves = 0
        while is_run and cnt_moves < len(san):
            if not stu:
                break
            if san[0] == stu[0]:
               san.popleft()
               stu.popleft()
               cnt_moves =0
            elif san[0] != stu[0]:
               move = stu.popleft()
               stu.append(move)
               cnt_moves +=1
        return len(stu)
               
            
            
            
               
            
            
    