from ast import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        answer = [0] * n
        stk = []

        # enumerate will return index to i and the value of index i to t
        for i, t in enumerate(temps):
            # white the stk is not empty and the temperature at the top of the stack is less than the current temperature, we keep poping
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()    # we found an answer for this index
                answer[stk_i] = i - stk_i   # get the distance

            stk.append((t,i)) # append the tuple of the current temperature and index

        return answer

        # TIME: O(n)
        # SPACE: O(n)

        