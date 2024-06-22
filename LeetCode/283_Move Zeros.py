#06/13/2024 Attempt 1
#res: https://leetcode.com/problems/move-zeroes/solutions/5320874/python-100-beat-100-efficient-optimal-solution-easy-to-understand/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_p = 0
        zero_i = len(nums) - nums.count(0)
        # non_p = len(nums) - 1
        non_p = zero_p + 1
        
        while zero_p < zero_i:
            if nums[zero_p] != 0:
                zero_p += 1
                # if ()
            else:
                non_p = zero_p + 1
                # if non_p < len(nums):
                while nums[non_p] == 0:
                    # by counting the number of zeros in nums, and determining the first index of zero of the correct $ array, we guarantee that if we are in the loop
                    ## we are not yet done CONFIRMING that all zeros are in the correct place towards the back of the array (zero_p < zero_i)
                    ## if we are in this else statement, then it is a fact that a zero was found in the non-zero partition of the nums array
                    ### therefore, we do not need to have a seperate check that ensures that the non_p index pointer will be within bounds of nums because logically there MUST be a non-zero element potentially in the zero partition
                    non_p += 1

                nums[zero_p] = nums[non_p]
                nums[non_p] = 0
