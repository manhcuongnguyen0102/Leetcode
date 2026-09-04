class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        p=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:# 1 o dat = 4 canh chi vi
                    p+=4
                    if row > 0 and grid[row-1][col]==1: # 2 o lien nhau ben tren -2 tong
                        p-=2
                    if col < cols-1 and grid[row][col+1]==1: # 2 o line nhau nhin ben phai
                        p-=2
        return p
            
        
# chu vi  =( so o 1*4)- (so o lien *2)
        