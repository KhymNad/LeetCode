# 278. First Bad Version (Easy)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        current_bad = 0

        # lo converges to the first bad version
        while lo <= hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid): # true, the current bad value, move hi down
                current_bad = mid
                hi = mid -1
            else: #(isBadVersion(mid) == False) move lo up
                lo = mid + 1
            
        return current_bad

        # TIME: O(log n)
        # SPACE: O(1)