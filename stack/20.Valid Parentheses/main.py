class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) <= 1:
            return False
        for _ in s:
            if _ =='(' or _ =='['or _=="{":
                stack.append(_)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if _ == ')' and top!= '(':
                    return False
                if _ == ']' and top!= '[':
                    return False
                if _ == '}' and top!= '{':
                    return False              
   
        if len(stack) == 0:
            return True
        else: return False
        