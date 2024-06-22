#06/17/2024 Attempt #1
# class Solution(object):
#     def findDifference(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[List[int]]
#         """
        
#         ans = list()
#         distinct_n1 = list()
#         distinct_n2 = list()

#         for num in nums1:
#             if num not in nums2 and num not in distinct_n1:
#                 distinct_n1.append(num)

#         for num in nums2:
#             if num not in nums1 and num not in distinct_n2:
#                 distinct_n2.append(num)

#         ans.append(distinct_n1)
#         ans.append(distinct_n2)

#         return ans

#06/17/2024 Attempt #2
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        n1set = set(nums1)
        n2set = set(nums2)
        ans = list()
    
        ans.append(list())
        for n1 in n1set:
            if n1 not in n2set:
                ans[0].append(n1)

        ans.append(list())
        for n2 in n2set:
            if n2 not in n1set:
                ans[1].append(n2)

        return ans