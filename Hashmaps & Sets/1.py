# 1. Two Sum (Easy)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        # populate the hashmap, keys = num in nums, values = index of num
        for i in range(len(nums)):
            h[nums[i]] = i
        
        # iterate through nums and subtract from target and lookup (O(1)) in hashmap for second value
        for i in range(len(nums)):
            y = target - nums[i]

            if y in h and h[y] != i:
                return[i, h[y]]

        # TIME: O(n)
        # SPACE: O(n)