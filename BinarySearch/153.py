## 153. Find Minimum in Rotated Sorted Array (Medium)

class Solution:
    def findMin(self, nums: List[int]) -> int:
                # INTUITION: the elements are just shifted over, we run Binary search but check for the lower range between the left or right side, we search that side for the pivot point (goes from increasing to decreasing)
        lo = 0
        hi = len(nums) - 1
        curr = min(nums[lo], nums[hi])

        # no need to search single list
        if len(nums) == 1:
            return nums[0]

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < curr:    # new min val
                curr = nums[mid]
            elif mid - 1 > 0 and nums[mid - 1] < nums[hi]:  # check if left side has a lower range
                hi = mid - 1
            else: #mid + 1 < len(nums) and nums[mid + 1] < nums[lo]:
                lo = mid + 1
        return curr

        # TIME: O(n)
        # SPACE: O(1)