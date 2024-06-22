#07/17/2024 Attempt #1
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pivot = 0
        left = 0
        right = 0
        
        for i in range(1, len(nums)):
            right += nums[i]

        while right != left or pivot < len(nums):
            pivot += 1

            left += nums[pivot - 1]
            right -= nums[pivot]

        if right == left:
            return pivot
        else:
            return -1

        