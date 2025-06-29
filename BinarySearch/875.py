# 875. Koko Eating Bananas (Medium)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Intuition:
        # We want to find the minimum eating speed k so that Koko can finish all the banana piles within h hours.
        # The slower she eats (smaller k), the longer it takes.
        # For any candidate k, we can compute how many hours it would take by summing up ceil(p / k) for all piles.
        # Since the total hours needed decreases as k increases (monotonic), we can use predicate binary search:
        # - Define k_works(k) = True if k is fast enough to finish in h hours.
        # - Search for the smallest k where k_works(k) becomes True.

        # Helper function: checks if eating speed k is enough to finish all piles within h hours
        def k_works(k):
            hours = 0
            for p in piles:
                # For each pile, calculate how many hours it takes to eat it at speed k
                hours += ceil(p / k)
            # Predicate: does this k satisfy the constraint?
            return hours <= h
        
        l = 1
        r = max(piles)  # Maximum possible speed (if we eat a whole pile in one hour)

        # DOES NOT WORK - this is because the time complexity of this implementation is O(n * len(piles)), does not work for large list size
        # Brute force approach: try every k from 1 to max(piles)
        # for k in range(1, r+1):
        #     if k_works(k):
        #         return k

        # Binary search to find the smallest k satisfying k_works(k)
        # This is predicate binary search: k_works(k) is monotonic (if True for k, then also True for all k > k)
        while l < r:
            k = (l + r) // 2  # Candidate speed
            if k_works(k):
                # If k works, try smaller speeds (look left)
                r = k
            else:
                # If k does not work, need a higher speed (look right)
                l = k + 1
        
        # When l == r, we have found the minimum k satisfying k_works
        return l

        # TIME: O(n * log(max(piles))
        # SPACE: O(1)