class Solution:
    def isPalindrome(self, s: str) -> bool:
        fill = [char.lower() for char in s if char.isalnum()]
        return fill[::]==fill[::-1]