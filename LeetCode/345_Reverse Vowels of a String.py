import re

#06/11/24 Attempt 1
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = list(s)

        vowels = re.compile(r'[aeiouAEIOU]')

        left = 0
        right = len(s) - 1
        both = 0

        while (left < right):
            if (re.match(vowels, sl[left])):
                both += 1
            else:
                left += 1
            
            if (re.match(vowels, sl[right])):
                both += 1
            else:
                right -= 1

            if (both == 2):
                temp = sl[left]
                sl[left] = sl[right]
                sl[right] = temp
                left += 1
                right -= 1
                
            both = 0

        string = ''.join(sl)
        return string
            
            