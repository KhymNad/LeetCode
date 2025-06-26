from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1

        while i < j:
            # This is a old method to swap elements, python can simplify this process
            # temp = s[i]
            # s[i] = s[j]
            # s[j] = temp

            # modern approach to swapping elements
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        # TIME: O(n)
        # SPACE: O(1)
