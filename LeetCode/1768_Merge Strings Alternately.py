# 6/7/24 attempt 1
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        if (len(word1) == 0 and len(word2) == 0):
            return ''
        elif (len(word1) == 0):
            return word2
        elif (len(word2) == 0):
            return word1
        else:
            merge_str = ''
            shorter_length = min(len(word1), len(word2))
            curr = 0
            while (curr < shorter_length):
                print(merge_str)
                merge_str += word1[0]
                merge_str += word2[0]
                word1 = word1[1:]
                word2 = word2[1:]
                curr += 1

            if (len(word1) < len(word2)):
                merge_str += word2[0: len(word2)]
            elif (len(word1) > len(word2)):
                merge_str += word1[0: len(word1)]
            
            return merge_str
        
class Solution(object):
    def mergeAlternately(self, word1, word2):

        max_len = max(len(word1), len(word2))

        i = 0
        merged = ''
        while (i < max_len):
            merged += (word1[i] or '') + (word2[i] or '')

        return merged
    
# 6/8/24 attempt 1  
class Solution(object):
    def mergeAlternately(self, word1, word2):

        max_len = max(len(word1), len(word2))
        merged = ''

        for i in range(max_len):
            if (i < len(word1)):
                merged += word1[i]
            if (i < len(word2)):
                merged += word2[i]

        return merged