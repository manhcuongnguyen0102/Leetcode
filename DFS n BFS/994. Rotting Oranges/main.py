from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols  = len(grid[0])
        minutes = 0
        cnt_fresh =0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cnt_fresh+=1
                elif grid[r][c] ==2:
                    queue.appendleft((r,c))
        if cnt_fresh == 0:
            return 0
        orientation = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue and cnt_fresh >0:
            current_rotten  = len(queue)
            for _ in range(current_rotten):
                r,c = queue.popleft()
                for dr,dc in orientation:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        cnt_fresh-=1
                        queue.append((nr,nc))
            
            minutes+=1    
        if cnt_fresh > 0:
            return -1
        else:
            return minutes
        
            