# 07/16/2024 Attempt 1
# from collections import Counter

# class Solution(object):
#     def closeStrings(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: bool
#         """
        
#         # OP1: Swap any two existing characters
#         ## basically if the two are the same un

#         #OP2: Transform every occurence of one existing character into another existing character, and do the same with the other character.

#         w1_dict = dict()
#         w2_dict = dict()

#         for w in word1:
#             w1_dict[w] = w1_dict.get(w, 0) + 1
#         for w in word2:
#             w2_dict[w] = w2_dict.get(w, 0) + 1

#         if len(word1) != len(word2) or set(word1) != set(word2) or Counter(w1_dict.values()) != Counter(w2_dict.values()):

#             return False
#         # elif set(word1) != set(word2):
#         #     return False
#         # elif 

# 07/16/2024 Attempt 2
# res: https://leetcode.com/problems/determine-if-two-strings-are-close/solutions/4561223/beats-99-46-users-c-java-python-javascript-explained/
from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        # OP1: Swap any two existing characters
        ## basically if the two are the same un

        #OP2: Transform every occurence of one existing character into another existing character, and do the same with the other character.

        w1_dict = dict()
        w2_dict = dict()

        for w in word1:
            w1_dict[w] = w1_dict.get(w, 0) + 1
        for w in word2:
            w2_dict[w] = w2_dict.get(w, 0) + 1

        w1c = Counter(w1_dict.values())
        w2c = Counter(w2_dict.values())
        # print(w1c)
        # print(w2c)
        if len(word1) != len(word2) or set(word1) != set(word2) or w1c != w2c:
            return False
        return True
        # if len(word1) != len(word2):
        #     print('1')
        #     return False
        # elif set(word1) != set(word2):
        #     print('2')
        #     return False
        # elif w1c != w2c:
        #     print('3')
        #     return False
        # else:
        #     return True