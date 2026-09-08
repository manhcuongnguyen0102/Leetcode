
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for char  in tokens:
            if char == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
            elif char == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
            elif char == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a*b)
            elif char == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(a/b))
            else:
                stack.append(char)
            
                                                                
        return int(stack[0]) 