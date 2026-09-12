class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        for char in text:
            count[char] = count.get(char,0)+1
        s="balloon"
        is_running = True
        cnt = 0
        while is_running :
            for char in s:
                if char in count and count[char]>0:
                    count[char]-=1
                else:
                    is_running = False
                    break
            if is_running == False:
                break
            else: 
                cnt+=1
        return cnt
            
            