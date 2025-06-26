from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                # the current value is greater than the target so we must decrease the value by moving the right pointer down
                right -= 1
            else:
                # the current value is less than the target so we must increase the value by moving the left pointer up
                left += 1

        # TIME: O(n)
        # SPACE: O(1)