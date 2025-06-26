
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the list is empty or has one element, it's already unique
        if not nums:
            return 0

        # Pointer i keeps track of the position of the last unique element
        i = 0

        # Start j from 1 and move through the array
        for j in range(1, len(nums)):
            # If current element is different from the last unique one
            if nums[j] != nums[i]:
                i += 1               # move i to the next position
                nums[i] = nums[j]   # update value at i to the new unique number

        # Return count of unique elements, which is i + 1
        return i + 1