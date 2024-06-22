# 06/15/2024 Attempt 1
# class Solution(object):
#     def longestOnes(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
        
#         max_ones = 0
#         left_ones = 0
#         right_ones = 0

#         curr_ones = 0
#         for j in range (0, k):
#             if nums[j] == 1:
#                 curr_ones += 1
            
#         i = 0

#         while i <= len(nums) - k:

# 06/15/2024 Attempt 2
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        flips = k
        head = 0
        tail = 0
        curr = 0
        most = 0

        while head < len(nums):
            if nums[head] == 0 and flips > 0:
                flips -= 1
                curr += 1
            elif nums[head] == 0 and flips <= 0:
                if flips < 0:
                    print('never print')

                while nums[tail] != 0: #sacrifice the ones until we find the 'nearest' 0
                    curr -= 1
                    tail += 1
                
                curr -= 1
                tail += 1
                curr += 1
            elif nums[head] == 1:
                curr += 1

            if curr > most:
                most = curr

            head += 1

        return most
        