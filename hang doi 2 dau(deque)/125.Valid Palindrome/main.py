from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        in_queue = deque()
        for char in s:
            if  65<= ord(char)<=90 :
                in_queue.append(char.lower())
            elif 97<=ord(char)<=122 or 48<=ord(char)<=57:
                in_queue.append(char)
            else:
                continue
        while len(in_queue)>1:
            if in_queue.popleft()!= in_queue.pop():
                return False
        return True
        