def isSubsequence(self, s, t):
        """
        :type s: str    the subsequence
        :type t: str    the orig. string
        :rtype: bool
        """

        subIndex = 0
        origIndex = 0

        # Loop through the full string and find all letters in the order of the substring
        while origIndex < len(t) and subIndex < len(s):
            if t[origIndex] == s[subIndex]:
                subIndex += 1
            origIndex += 1

        if subIndex == len(s):
            return(True)
        else:
            return(False)