from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # if there is only one item in the list, that is the ans.
        closest = nums[0]
        for x in nums:  # O(n)
            # if the absolute value of the current item is less than the abs. value of the current closest item, then we have found a new closest item
            if abs(x) < abs(closest):
                closest = x
        # account for the occurence of 2 closest numbers by checking for the larger value within the nums list
        if closest < 0 and abs(closest) in nums: # O(n)
            return abs(closest)
        else:
            return closest

        # Time complexity: O(2n) =(reduces)=> O(n)
        # Space: O(1) - not using any sort of storage 

