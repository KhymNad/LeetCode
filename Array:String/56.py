from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # This sorts the list based on the start times (interval[0])
        intervals.sort(key = lambda interval: interval[0])
        merged = []

        for interval in intervals:
            # if the merged array is empty or the latest appended interval's ending value is less than the current interval's starting value (no overlap), than we append the current interval in intervals
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else: # There is overlap
                # the last interval in merged has overlap with the current interval in intervals and so we don't need to update the last intervals starting point (merged[-1][0]), but we need to update the ending value which is why we need to do max(merged[-1][1], interval[1])
                merged[-1] = merged[-1][0], max(merged[-1][1], interval[1])

        return merged
        # Time: O(n log n)
        # Space: O(n)
