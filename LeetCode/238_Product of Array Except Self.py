
#06/12/24 Attempt 1
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = list()

        total_product = 1
        pref = list()
        suff = [1] * len(nums)

        #pref
        pref.append(1)
        for i in range (1, len(nums)):
            pref.append(pref[i - 1] * nums[i - 1])

        #suff
        suff[len(nums) - 1] = 1 
        for i in range (len(nums) - 2, -1, -1):
           suff[i] = suff[i + 1] * nums[i + 1]

        prod = list()
        for i in range (0, len(nums)):
            # prod[i] = suff[i] * pref[i]
            prod.append(suff[i] * pref[i])

        return prod 