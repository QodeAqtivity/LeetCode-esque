# 6/8/24 attempt 1
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        curr_alt = 0
        max = 0
        
        for x in gain:
            curr_alt += x
            if (curr_alt > max):
                max = curr_alt

        return max

#6/15/24 attempt 2
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        curr = 0
        most = 0

        for g in gain:
            curr += g

            if curr > most:
                most = curr
        
        return most