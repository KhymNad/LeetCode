# 1004. Max Consecutive Ones 111 {Medium}

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Intuition:
        # Use a sliding window approach to find the longest subarray
        # containing only 1s with at most k zeros flipped to 1s.

        max_w = 0                # Tracks the maximum length of a valid window
        num_zeros = 0            # Counts zeros in the current window
        left = right = 0         # Initialize window pointers

        while right < len(nums):
            if nums[right] == 1:
                # If current element is 1, expand window to the right
                right += 1
                if (right - left) > max_w:
                    max_w = right - left

            elif nums[right] == 0 and num_zeros < k:
                # If it's a 0 and we still have flips remaining, include it
                right += 1
                num_zeros += 1 
                if (right - left) > max_w:
                    max_w = right - left

            elif nums[right] == 0 and num_zeros >= k:
                # If no flips left, shrink window from the left
                if nums[left] == 1:
                    left += 1  # Simply move past a 1
                else:
                    left += 1  # Move past a 0 and "unflip" it
                    num_zeros -= 1
                    
        return max_w

        # TIME: O(n)
        # SPACE: O(1)