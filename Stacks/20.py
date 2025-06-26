class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            elif bracket == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                else:
                    stack.pop(-1)
            elif bracket == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                else:
                    stack.pop(-1)
            elif bracket == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                else:
                    stack.pop(-1)
            else:
                return False

        if len(stack) != 0:
            return False
        else:
            return True

        # TIME: O(n), SPACE: O(n)