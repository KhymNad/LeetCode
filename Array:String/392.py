class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if s == '': return True # an empty string is a subsequence of the parent string
        if S > T: return False  # a substring can not be longer than the parent string 

        j = 0 # index for s
        for i in range(T):
            if t[i] == s[j]:
                if j == S-1: # we have reached the end of the substring         
                    return True
                j += 1

        return False

        # Time: O(T)
        # Space: O(1)


    