# 771. Jewels and Stones (Easy)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        
        return count

        # TIME: O(n + m) - Creating the set takes O(m), scanning the stones takes O(n)
        # SPACE: O(m) - to store the jewelset