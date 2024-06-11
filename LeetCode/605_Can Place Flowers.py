from mylibrary import ceilingDiv

# 6/11/24 Attempt 1
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        base_flowers = flowerbed.count(1)
        
        # if len(flowerbed) // 2 > n:
        #     # the most amount of flowers you can have in the flowerbed is (floor) half of the number 

        #     return False
        # if ceilingDiv(len(flowerbed), 2) - base_flowers < n:
        if (-(len(flowerbed) // -2)) - base_flowers < n:
            # the most amount   of flowers you can have in the flowerbed is (floor) half of the number of plots
            ## but you must also consider the flowers already in there 
            return False
        #technically enough plots but could be suboptimal
        elif (len(flowerbed) == 1):
            if ((n == 0) and (flowerbed[0] in [0, 1])) or ((n == 1) and (flowerbed[0] == 0)):
                return True
            else:
                return False
        else:
            flowers_left = n
            for i in range(0, len(flowerbed)):
                if (i == 0):
                    if (flowerbed[i] == 0 and flowerbed[i+1] == 0):
                        flowerbed[i] = 1
                        flowers_left -= 1
                elif (i == len(flowerbed) - 1):
                    if (flowerbed[i] == 0 and flowerbed[i-1] == 0):
                        flowerbed[i] = 1
                        flowers_left -= 1
                else:
                    if (flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                        flowerbed[i] = 1
                        flowers_left -= 1

            if flowers_left <= 0:
                return True
            else:
                return False 
                    