# 643. Maximum Average Subarray I (Easy)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Intuition:
        # We want to find the contiguous subarray of length k with the maximum average.
        # Instead of recomputing the sum of each window from scratch, we use a sliding window:
        # - Start by summing the first k elements.
        # - Then, for each new element, add it to the current sum and remove the element that is sliding out.
        # This way, we maintain the sum in O(1) time per step.
        # Finally, we keep track of the maximum average seen so far.

        n = len(nums)
        cur_sum = 0

        # Compute the sum of the first window of size k
        for i in range(k):
            cur_sum += nums[i]

        # Initialize the maximum average with the first window
        max_avg = cur_sum / k

        # Slide the window across the array
        for i in range(k, n):
            # Add the new element to the window
            cur_sum += nums[i]
            # Remove the element that slid out of the window
            cur_sum -= nums[i - k]

            # Compute the average of the current window
            avg = cur_sum / k
            # Update max_avg if this window's average is higher
            max_avg = max(max_avg, avg)

        return max_avg

        # TIME: O(n) 
        # SPACE: O(1)
