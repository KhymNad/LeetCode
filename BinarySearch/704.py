from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (hi + lo // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else: # nums[mid] > target
                hi = mid - 1
        
        return -1



