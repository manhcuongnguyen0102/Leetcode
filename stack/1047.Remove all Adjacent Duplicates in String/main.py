class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for _ in s:
            if stack and stack[-1] == _:
                stack.pop()
            else:
                stack.append(_)
        return  ("".join(stack))