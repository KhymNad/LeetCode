# 1189. Maximum Number of Balloons (easy)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        for char in text:
            print("char: ", char)
            if char in hashmap:
                hashmap[char] += 1
                print("hashmap: ", hashmap)

        # Adjust for letters that appear twice in "balloon"
        hashmap["l"] //= 2
        hashmap["o"] //= 2

        # Minimum frequency among all required letters
        return min(hashmap.values())

        # TIME: O(n)
        # SPACE: O(1)