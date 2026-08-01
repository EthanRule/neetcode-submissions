class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s:
            if s[0] == ')' or s[0] == ']' or s[0] == '}':
                return False

        for char in s:
            #check wrong way first element

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
        