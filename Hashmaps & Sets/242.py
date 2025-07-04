# 242. Valid Anagram (easy)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = Counter(s) # convert s into a hashmap depicting the occurence of each char in s

        if len(s) != len(t):
            return False

        for char in t: # iterate through all characters in t
            if char in hashmap:
                if hashmap[char] > 0: # check occurences of char
                    hashmap[char] -= 1
                else:
                    return False
            else:
                return False

        return True

        # TIME: O(M + N) -> M = TC to convert s to hashmap, N = iterate through t
        # SPACE: O(M) -> size of hashmap


        # MORE OPTIMAL SOLUTION
        if len(s) != len(t):
            return False
        
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
    
        # TIME: O(n)
        # SPACE: O(n)