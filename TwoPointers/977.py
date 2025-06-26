from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:    # left pointer and right pointer have not crossed
            if abs(nums[left]) > abs(nums[right]):  # append the grater value to the list
                result.append(nums[left] ** 2)
                left += 1
            else:   # append the greater value to the lsit
                result.append(nums[right]**2)
                right -= 1
        # NOTE: we always append the greater value because the nums array is initially sorted in non-decreasing order


        result.reverse() # reverse the list, this is a constant operation

        return(result)

        # TIME: O(n)
        # SPACE: O(n) - O(1) is we ignore the extra space we are required to use to return the answer (result list)
