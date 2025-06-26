class Solution:
    def romanToInt(self, s: str) -> int:
        # this is how to implement a hash map inorder to look up symbol to value pairs
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}

        summ = 0
        n = len(s)
        i = 0

        while i < n:
            # edge case to not evaluate a roman numeral that does not exist, i.e. look outside the string
            if i < n - 1 and d[s[i]] < d[s[i+1]]:
                # the current numeral at i is less than the numeral infront of it so we subtract, and since we evaluated 2 numerals together we move up 2 spaces
                summ += d[s[i+1]]- d[s[i]]
                i += 2
            else:
                # the opposite case, the current numeral is grater than the numeral at i + 1 so we evaluate the singal numeral, i.e. add it to summ and move up 1 space
                summ += d[s[i]]
                i += 1

        return summ
        # Time O(n)
        # Space O(1)