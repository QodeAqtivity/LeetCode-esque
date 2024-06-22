#06/15/2024 Attempt 1
#res: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/solutions/4985060/simple-implementation-using-sliding-window-but-only-in-constant-space-o-n-time-complexity-easy/
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        vowels = ['a', 'e', 'i', 'o', 'u'] #only lower case letters

        max_v = -1
        curr_v = 0

        for j in range (0, k):
            if s[j] in vowels:
                curr_v += 1
                   
        max_v = curr_v

        i = 1
        while i <= len(s) - k:
            if s[i-1] in vowels:
                curr_v -= 1

            if s[i-1+k] in vowels:
                curr_v += 1            

            if curr_v > max_v:
                max_v = curr_v

            i += 1

        return max_v
    
solution = Solution()
solution.maxVowels('weallloveyou', 7)