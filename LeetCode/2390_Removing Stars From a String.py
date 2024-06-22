#07/17/2024 Attempt 1
# class Solution(object):
#     def removeStars(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
        
#         string_stack = list(s)
#         star_count = string_stack.count('*')
#         i = len(s) - 1

#         while star_count != 0 or i >= 0:
#             if string_stack[i] == '*':  # and star_count > 0:
#                 string_stack.pop(i)
#                 i -= 1
#                 star_count -= 1
#                 while string_stack[i] != '*':
#                     string_stack.pop(i)
#                     i -= 1
#                 string_stack.pop(i) # if string_stack[i] == '*':
#                 i -= 1
#                 star_count -=1
#             i -= 1


#         return ''.join(string_stack)

#07/17/2024 Attempt 2
# class Solution(object):
#     def removeStars(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """

#07/17/2024 Attempt 3
# class Solution(object):
#     def removeStars(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
        
#         string_stack = list(s)
#         star_count = string_stack.count('*')
#         i = len(s) - 1

#         while star_count != 0 and i >= 0:
#             if string_stack[i] == '*':  # and star_count > 0:
#                 string_stack.pop(i)
#                 i -= 1
#                 star_count -= 1
#                 while string_stack[i] != '*':
#                     print(string_stack)
#                     string_stack.pop(i)
#                     i -= 1
#                 string_stack.pop(i) # if string_stack[i] == '*':
#                 i -= 1
#                 star_count -=1
#             else:
#                 i -= 1

#         print(''.join(string_stack))
#         return ''.join(string_stack)

# solution = Solution()
# solution.removeStars("lee*t**cod*e")

#07/17/2024 Attempt 4
# class Solution(object):
#     def removeStars(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """

#         s_stack = list(s)
#         count = s_stack.count('*')
#         i = len(s_stack)

#         while count > 0 and i >= 0:
#             if s_stack[i] == '*':
#                 s_stack.pop(i)
#                 i -= 1
#                 pop_count = 1
#                 count -= 1 

#                 while pop_count > 0 :
#                     if s_stack[i] == '*':
#                         s_stack.pop(i)
#                         i -= 1
#                         pop_count += 1
#                         count -= 1
#                     else:
#                         s_stack.pop(i)
#                         i -= 1
#                         pop_count -= 1
#             else:
#                 i -= 1

#         return ''.join(s_stack)

#07/17/2024 Attempt 5
# class Solution(object):
#     def removeStars(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """

#         s_stack = list(s)
#         count = s_stack.count('*')
#         i = len(s_stack) - 1

#         while count > 0 and i >= 0:
#             if s_stack[i] == '*':
#                 s_stack.pop(i)
#                 i -= 1
#                 pop_count = 1
#                 count -= 1 

#                 while pop_count > 0 :
#                     if s_stack[i] != '*':
#                         pop_count -= 1
#                     else:
#                         pop_count += 1
#                         count -= 1
                    
#                     s_stack.pop(i)
#                     i -= 1
#             else:
#                 i -= 1

#         return ''.join(s_stack)

#07/17/2024 Attempt 6
#res: https://leetcode.com/problems/removing-stars-from-a-string/solutions/3402529/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = list()

        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()

        return ''.join(stack)