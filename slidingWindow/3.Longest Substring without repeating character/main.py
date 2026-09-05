class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_len = 0
        for right,value in enumerate(s):
            if value in seen and seen[value]>= left:
                left = seen[value]+1
            seen[value] = right
            current_len = right - left +1
            if current_len > max_len:
                max_len = current_len
        return max_len
            