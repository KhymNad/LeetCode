from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        element1 = 0
        element2 = 0

        for item in operations:
            if item == '+':
                element1 = stack[-2]
                element2 = stack[-1]
                stack.append(element1 + element2)
            elif item == 'D':
                element1 = stack[-1]
                stack.append(element1 * 2)
            elif item == 'C':
                stack.pop()
            else:
                stack.append(int(item))
            element1 = 0
            element2 = 0
        
        return sum(stack)

        # TIME: O(n)
        # SPACE: O(n) - if the answer stack is not considered: O(1)
            