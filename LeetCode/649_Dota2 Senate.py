# 07/19/2024 Attempt 1
# class Solution(object):
#     def predictPartyVictory(self, senate):
#         """
#         :type senate: str
#         :rtype: str
#         """
        
#         # for i in range (0, len(senate)):
#             # if len(senate) == 1:
#             #     if senate[0] == 'R':
#             #         return 'Radiant'
#             #     else: #elif senate[0] == 'D':
#             #         return 'Dire'
#             # else: 
#         q = list(senate)
#         i = 0
#         while i < len(q):
#             x = i + 1 if i < len(q) - 1 else 0
#             while x != i and (q[i] == q[x]): # if full loop then break; if different senate party then break
#                 if x == len(q) - 1:
#                     x = 0
#                 else:
#                     x += 1
            
#             if x == i:
#                 return 'Radiant' if q[i] == 'R' else 'Dire'
#             else:
#                 q.pop(x)
#                 i += 1
#         return 'Radiant' if q[0] == 'R' else 'Dire'
    
# 07/19/2024 Attempt 2
# class Solution(object):
#     def predictPartyVictory(self, senate):
#         """
#         :type senate: str
#         :rtype: str
#         """
        
#         q = list(senate)
#         i = 0
#         # while i < len(q):
#         while len(q) != q.count('R') and len(q) != q.count('D'):
#             x = i + 1 if i < len(q) - 1 else 0
#             while x != i and (q[i] == q[x]): # if full loop then break; if different senate party then break
#                 x = x + 1 if x < len(q) - 1 else 0
#                 # if x == len(q) - 1:
#                 #     x = 0
#                 # else:
#                 #     x += 1
            
#             if x == i:
#                 return 'Radiant' if q[i] == 'R' else 'Dire'
#             else:
#                 q.pop(x)
#                 i = i + 1 if i < len(q) - 1 else 0
#                 # i += 1
#         return 'Radiant' if q[0] == 'R' else 'Dire'

# 07/19/2024 Attempt 3
# sol: https://www.youtube.com/watch?v=zZA5KskfMuQ
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        
        q = list(senate)
        radiant_queue = list()
        dire_queue = list()
        offset = len(senate)

        for i in range (0, len(senate)):
            if senate[i] == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while radiant_queue and dire_queue:
            r = radiant_queue.pop(0)
            d = dire_queue.pop(0)

            # never should r == d (in terms of indices)
            if r > d:
                radiant_queue.append(r + offset)
            else:
                dire_queue.append(d + offset)

        return 'Radiant' if radiant_queue else 'Dire'


solution = Solution()
solution.predictPartyVictory("RD")