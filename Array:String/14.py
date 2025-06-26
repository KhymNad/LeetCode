from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')

        # we want to find the minimum length string first to avoind out of bounds errors
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
        # we want to compare all the characters in each string to the chracters in the first string of the strs array and up until the minimum_length of the sortest string
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]: # compare each strings char to the char of the first string in strs
                    return s[:i]    # return the substring up until the point where the chars are not equal, this syntax is not inclusive
            i += 1

        return s[:i] # this covers the edge case where the strs array has not problems in the above loop, i.e. the array is simple [""] or ["a"]

        # Time: O(n * m) - For and while loops
        # Space: O(1)