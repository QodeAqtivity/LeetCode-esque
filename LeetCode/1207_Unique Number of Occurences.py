#06/17/2024 Attempt 1
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occur_dict = dict()

        for n in arr:
            if n in occur_dict:
                occur_dict[n] += 1
            else:
                occur_dict[n] = 1

        occur_set = set()

        for key in occur_dict:
            if occur_dict[key] in occur_set:
                return False
            else:
                occur_set.add(occur_dict[key])
        
        return True

#06/17/2024 Attempt 2
#res: https://leetcode.com/problems/unique-number-of-occurrences/solutions/4577893/beats-100-users-c-java-python-javascript-2-approaches-explained/
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        freq = dict()

        for n in arr:
            freq[n] = freq.get(n, 0) + 1
        
        return len(freq) == len(set(freq.values()))