# 3. Longest Substring Without Repeating Characters (Medium)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Intuition:
        Use a sliding window to find the longest substring without repeating characters.
        We expand the window by moving the `right` pointer as long as the character at `right`
        is not already in the current window (`s[left:right]`). If a duplicate is found, we move
        the `left` pointer to shrink the window until the duplicate is removed.
        At each step, we track the length of the current valid window and update the maximum length.
        """

        # Initialize two pointers: left and right
        left, right = 0, 1
        curr = 1          # current window length (starts at 1 because right starts at index 1)
        max_len = 0       # keeps track of the maximum length found

        # Edge case: single character string
        if len(s) == 1:
            return 1

        # Iterate until the right pointer reaches the end of the string
        while right < len(s):
            # Check if the current character at `right` is not in the current window
            if s[right] not in s[left:right]:
                # Valid window, extend it and update current and max length
                curr = (right - left) + 1
                max_len = max(curr, max_len)
                right += 1
            else:
                # Found a duplicate character, move left to shrink the window
                left += 1
                curr = 0  # reset current count since we’ll recalculate in next valid window

        return max_len

        # TIME: O(n)
        # SPACE: O(1)
