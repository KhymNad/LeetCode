# 383. Ransom Note (Easy)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine) # TC for counter is O(n)

        for letter in ransomNote:
            if hashmap[letter] > 0: # TC for hashmap lookup is O(1)
                hashmap[letter] -=1 # TC for hashmap update is O(1)
            else:
                return False

        return True

        # TIME: O(R + M) -> R = len(ransomeNote), M = len(magazine)
        # SPACE: O(M) -> when using a hashmap
            