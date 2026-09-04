class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        current_color = image[sr][sc]
        if color == current_color:
            return image
        rows = len(image)
        cols = len(image[0])
        def df(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0:
                return 
            if image[r][c] != current_color:
                return
            
            image[r][c] = color
            
            df(r+1,c)
            df(r-1,c)
            df(r,c+1)
            df(r,c-1)
        df(sr,sc)
        
        return image