# 217 Contains Duplicate (easy)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() 

        for num in nums:
            if num in seen: # Checking the set is O(1)
                return True
            else:
                seen.add(num)   # adding to the set is O(1)

        return False

        # TIME: O(n)
        # SPACE: O(n)  