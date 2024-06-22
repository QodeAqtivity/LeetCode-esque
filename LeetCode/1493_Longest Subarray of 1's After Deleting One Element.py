#07/15/2024 Attempt #1
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        most = 0
        curr = 0
        head = 0
        tail = 0
        flip = True

        while head < len(nums):
            if nums[head] == 0 and flip:
                flip = False
            elif nums[head] == 0 and not flip:
                while nums[tail] != 0:
                    curr -= 1
                    tail += 1
                
                curr -= 1
                tail += 1
                curr += 1
            elif nums[head] == 1:
                curr += 1
            
            head += 1

            if curr > most:
                most = curr

        # return most
        if flip:
            return most - 1
        else:
            return most
        