from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        # increment i through the array to find the answers
        for i in range(n):
            # if nums[i] > 0 the nall lo and hi index values will also be > 0 so there is no way to get a summ of 0
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                # loop i until a new nums[i] is found
                continue
            
            lo, hi = i+1, n-1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo+1, hi-1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        # find a new low value
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        # find a new high value
                        hi -= 1
                elif summ < 0:
                    lo += 1
                else: # summ is greater than 0 so decrease high to get a lower value 
                    hi -= 1

        return answer

        # TIME: O(n^2)
        # SPACE: O(n)