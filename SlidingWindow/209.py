# 209. Minimum Size Subarray Sum (medium)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Intuition:
        Use a sliding window approach to find the minimum length of a contiguous subarray
        whose sum is greater than or equal to the given target. 
        We expand the window by moving the right pointer and add to the sum.
        Once the sum becomes >= target, we try to shrink the window from the left
        as much as possible while still satisfying the condition. 
        The smallest valid window size encountered is our answer.
        """

        left = 0
        right = 0
        summ = 0              # running sum of the current window
        min_len = float('inf')  # initialize with infinity to track the minimum

        while right < len(nums):
            # Expand the window by including nums[right]
            summ += nums[right]

            if summ >= target:
                # Try shrinking the window from the left while the sum is still >= target
                while summ >= target:
                    # Update the minimum length if this window is smaller
                    min_len = min(min_len, right - left + 1)
                    # Shrink the window from the left
                    summ -= nums[left]
                    left += 1

                # Move right forward for next iteration
                right += 1

            else:
                # Sum is still less than target, expand the window
                right += 1

        # If min_len was never updated, return 0 (no valid subarray found)
        return 0 if min_len == float('inf') else min_len
