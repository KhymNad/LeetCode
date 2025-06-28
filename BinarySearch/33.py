# 33. Search in Rotated Sorted Array (Medium)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Intuition:
        The input array is a sorted array that has been rotated at some pivot.
        To search efficiently, we first find the index of the smallest element (the pivot),
        which splits the array into two sorted halves. Then we determine which half
        the target lies in and perform standard binary search on that half.
        """

        n = len(nums)
        l, r = 0, n - 1

        # Step 1: Find the index of the smallest element (rotation pivot)
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                # Pivot is to the right of m
                l = m + 1
            else:
                # Pivot is at m or to the left
                r = m
        min_i = l  # Index of the smallest element

        # Step 2: Decide which side of the pivot to search
        if min_i == 0:
            l, r = 0, n - 1  # Array is not rotated
        elif target >= nums[0] and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1  # Target is in the left sorted half
        else:
            l, r = min_i, n - 1  # Target is in the right sorted half

        # Step 3: Perform standard binary search
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1  # Target not found

        # TIME: O(log n * log n) = O(2log n) = O(log n)
        # SPACE: O(1)
