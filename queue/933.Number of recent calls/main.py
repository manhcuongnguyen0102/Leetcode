from collections import deque
class RecentCounter:

    def __init__(self):
        self.cnt = deque()
        

    def ping(self, t: int) -> int:
        self.cnt.append(t)
        while self.cnt[0] < t-3000:
            self.cnt.popleft()
        return len(self.cnt)
        
        
        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)