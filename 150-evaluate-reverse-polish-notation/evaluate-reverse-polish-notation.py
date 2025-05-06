class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char in '+-/*':
                b=stack.pop()
                a=stack.pop()
                if char =='-':
                    stack.append(a - b)
                elif char =='+':
                    stack.append(a + b)
                elif char =='*':
                    stack.append(a * b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(char))
        return stack[0]