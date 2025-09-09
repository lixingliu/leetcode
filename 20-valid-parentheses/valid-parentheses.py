class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = ["(", "{", "["]
        for bracket in s:
            if bracket in openBrackets:
                stack.append(bracket)
                continue
            if len(stack) == 0:
                return False
            if bracket == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif bracket == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False 
            elif bracket == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False