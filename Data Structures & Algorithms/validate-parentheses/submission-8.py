class Solution:
    def isValid(self, s: str) -> bool:
        chars = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for bracket in s:
            print(stack)
            if bracket in chars.keys(): # opening bracket, put closing on top
                stack.append(chars[bracket])
            elif stack and bracket == stack[-1]: # if closing bracket is top of stack
                stack.pop()
            else:
                return False
        
        return True if not stack else False
            