# 6/9/24 Attempt ...
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        # if str1 and str2 are composed of multiples of a string t, then they should have the same gcd (in terms of their lenght) as well
        # we are trying to find the greatest common denominator string/the longest common repeating/multiple string
        ## that means that str1 and str2 are only comprised of multiples of a common string
        ### if any point their characters diverge for a given index, then they do not have a gcd
        ### they should both be divisible by the same number and have a gcd



        # same_char
        
# 6/9/24
# $ src: https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3977616/python-solution-using-recursion-easy-to-understand/?envType=study-plan-v2&envId=leetcode-75
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 != str2 + str1:
            #only possible if str1 and str2 are solely compromised of a common string 't'
            #if this runs, this should only run once (during the first iteration)
            return ''        
        # if str1 and str2 were different in anyway (in terms of character composition not length), then the conditional above would not work
        # which means all the conditionals after operate under the assumption that str1 and str2 are made up of the same string 't' of same or varying multiples
        elif len(str1) == len(str2): 
            #str1 and str2 are the exact same string in both length and character composition
             return str1 # or str2 (doesn't matter)
        # the next two conditionals are using recursion to find the gcd string
        ## the longest the gcd string can be is one of the two strings' length
        # i am wondering if the bottom two are using a principle of the Euclidean Algorithm to ensure the gcd string is returned
        elif len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str1, str2[len(str1):])
