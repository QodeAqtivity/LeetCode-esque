#06/13/2024 Attempt 1
#res: https://leetcode.com/problems/is-subsequence/solutions/1811508/python-javascript-easy-solution-with-very-clear-explanation/
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        si = 0
        ti = 0

        if s == t: #same
            return True
        elif len(s) > len(t):
            return False

        #double for loop but essentially Big O (n) because limited by both indices being in range and generally speaking both arrays are being iterated over simulatenously, worse case scenario is that it is not a subsequence and we traverse all of s and t to find that out (missing one char to be subsequence)
        while si < len(s) and ti < len(t): #indices within bounds

            # while ti < len(t) and t[ti] != s[si]:
            while t[ti] != s[si]:
                ti += 1
                
                if ti >= len(t): #== should suffice
                    return False

            # if ti < len(t) and t[ti] == s[si]:
            if t[ti] == s[si]:  
                si += 1
                ti += 1    

        if si == len(s):
            return True
        else:
            return False
            