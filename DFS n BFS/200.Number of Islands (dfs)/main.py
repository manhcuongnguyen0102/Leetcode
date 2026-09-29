class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        visited = {}
        if not grid:
            return 0
        def dfs(r,c):
            if (r<0 or c<0 or r>=m or c>=n or grid[r][c] =='0' or (r,c) in visited):
                return
            visited[(r,c)] = True
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for i in range (m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    cnt+=1
                    dfs(i,j)   
        return cnt