# 6/9/24 Attempt 1
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        base_max = max(candies)
        most_candies = list()

        for candy in candies:
            if (candy + extraCandies >= base_max):
                most_candies.append(True)
            else:
                most_candies.append(False)

        return most_candies