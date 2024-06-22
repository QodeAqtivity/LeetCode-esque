#06/12/2024 Attempt 1
# class Solution(object):
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         curr_i = 0

#         while curr_i < len(nums):
#             if (curr_i == 0):
#                 if (nums[curr_i] < nums[curr_i + 1]) and (nums[curr_i + 1] < nums[curr_i + 2]):
#                     return True
#             elif(curr_i == len(nums) - 1):
#                 return False
#             else:
#                 if (nums[curr_i] > nums[curr_i - 1]) and (nums[curr_i] < nums[curr_i + 1]):
#                     return True
            
#             curr_i += 1
        
#         return False

#06/12/2024 Attempt 2
# res: https://leetcode.com/problems/increasing-triplet-subsequence/solutions/5287156/beats-99-simple-solution-explained-line-by-line-c-java-python/
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
                # second = float('inf')
            elif num <= second:
                second = num
            else:#implict that num is greater than first and second
                return True
            
        return False
    
    #[20,100,10,12,5,13] think of this example
    