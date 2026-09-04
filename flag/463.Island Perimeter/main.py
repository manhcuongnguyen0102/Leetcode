class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def df(r,c):
            cnt = 0
            if r == rows:
                cnt+=1
            if c == cols:
                cnt+=1
            if r < 0:
                cnt+=1
            if c < 0:
                cnt+=1
            if grid[r][c] == 0:
                cnt+=1
            if grid[r][c] == -1:
                cnt+=0
            
            grid[r][c]==-1
            
            df(r-1,c)
            df(r+1,c)
            df(r,c+1)
            df(r,c-1)
            return cnt
        p=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    p+=df(row,col)
        return p
            
        
        
        