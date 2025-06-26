from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i] # this is the start of the range

            # move i through the range of ints in the array if the next int is nums[i] + 1
            while i < len(nums) - 1 and nums[i]+1 == nums[i+1]:
                i += 1

            # the next int in the array is not nums[i] + 1 so append the range 
            if start != nums[i]:
                ans.append(str(start) + '->' + str(nums[i]))
            else:   # the range and the start are the same so append the single int
                ans.append(str(nums[i]))

            i += 1

        return ans

        # Time: O(n) - This is not O(n^2) because i is not being reset and is traversing the list a single time
        # Space: O(n) - storing the answer array


