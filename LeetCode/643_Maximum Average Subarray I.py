#06/13/2024 Attempt #1
#res: https://leetcode.com/problems/maximum-average-subarray-i/solutions/3726814/easy-solution-with-o-n-time/
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_max_i = 0
        curr_max = float('-inf')
        curr_sum = 0
        for i in range(0, k):
            curr_sum += nums[i]
        # prev_sum = 0
        i = 0

        while i <= len(nums) - k:
            if (i != 0):
                curr_sum -= nums[i-1]
                curr_sum += nums[i-1+k]

            if curr_max < curr_sum:
                curr_max = curr_sum
                curr_max_i = i

            i += 1
            # return nums[i:i+k]
        return float(curr_max) / k


solution = Solution()
print(solution.findMaxAverage([-1], 1))