class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def df(r,c):
            if r < 0 or c < 0 or r>=rows or c>=cols:
                return 1
            if grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0

            grid[r][c] =-1
            cnt = 0
            cnt+=df(r-1,c)
            cnt+=df(r+1,c)
            cnt+=df(r,c+1)
            cnt+=df(r,c-1)
            return cnt
            
        p=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    p+=df(row,col)
        return p
            
        
        
        