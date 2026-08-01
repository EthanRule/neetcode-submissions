class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            #add to stack
            if char == '(' or char == '{' or char == '[':
                stack.append(char)

            #peek top element for match and remove from stack
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False

            if char == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False

            if char == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False
        