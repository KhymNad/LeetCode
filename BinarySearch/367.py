# 367. Valid Perfect Square (Easy)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num

        while lo <= hi:
            mid = (lo + hi) // 2
            mid_squared = mid**2
            if mid_squared == num:
                return True
            elif mid_squared < num:
                lo = mid + 1
            else: # mid_squared > num
                hi = mid - 1
        
        return False