from ast import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        netGain = 0
        highestAlt = 0
        
        for i in range(len(gain)):
            netGain += gain[i]
            if netGain > highestAlt:
                highestAlt = netGain
        
        return(highestAlt)