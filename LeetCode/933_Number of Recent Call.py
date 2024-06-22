#6/17/24 Attempt #1
# class RecentCounter(object):

#     def __init__(self):
#         self.req = list()
#         self.rec_req = 0        

#     def ping(self, t):
#         """
#         :type t: int
#         :rtype: int
#         """
#         self.rec_req = 0
#         self.req.append(t)
        
#         # for i in range(0, len(self.req)):
#         i = len(self.req) - 1
#         while i >= 0:
#             # if self.req[i] <= t and self.req[i] >= t - 3000:
#             #     self.rec_req += 1
#             #     i -= 1
#             # else:
#             #     self.req = self.req[i+1:len(self.req)]
#             #     break
#             if self.req[i] >= t - 3000:
#                 self.rec_req += 1
#                 i -= 1
#             else:
#                 self.req = self.req[i+1:len(self.req)]
#                 break
                
#         return self.rec_req

#6/18/24 Attempt #1
#res: https://leetcode.com/problems/number-of-recent-calls/solutions/873209/python-super-simple-and-short-solution-o-1-time-o-1-space/
class RecentCounter(object):

    def __init__(self):
        self.req = list()      

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.req.append(t)

        # while t - self.q[0] > 3000:
        while self.req[0] < t - 3000: # lowerbound
            self.req.pop(0)

        return len(self.req)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)