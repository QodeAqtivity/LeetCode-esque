#06/18/24 Attempt 1
# class Solution(object):
#     def asteroidCollision(self, asteroids):
#         """
#         :type asteroids: List[int]
#         :rtype: List[int]
#         """
#         stack = list()

#         stack.append(asteroids[0])

#         for i in range (1, len(asteroids)):
#             curr_a = asteroids[i]
#             curr_last_i = len(stack) - 1

#             if (stack[curr_last_i] > 0  and curr_a > 0) or (stack[curr_last_i] < 0 and curr_a < 0): # same sign, not going to strike each other
#                 stack.append(curr_a)
#             else:
#                 stop = False

#                 while stop == False and curr_last_i >= 0:
#                     # if curr_last_i != 0:                    
#                         # logically all asteroids in the stack should be pointing in the same direction
#                         if abs(stack[curr_last_i]) < abs(curr_a):
#                             stack.pop()
#                             curr_last_i -= 1
#                         elif abs(stack[curr_last_i]) == abs(curr_a):
#                             stack.pop()
#                             stop = True
#                         else:
#                             stop = True
#                     # else:
#                     #     stack.append(curr_a)
#                     #     curr_last_i -= 1
#                 if curr_last_i < 0:
#                     stack.append(curr_a)

#         return stack

#06/18/24 Attempt 2
# class Solution(object):
#     def asteroidCollision(self, asteroids):
#         """
#         :type asteroids: List[int]
#         :rtype: List[int]
#         """

#         stack = list()
#         stack.append(asteroids[0])

#         for i in range (1, len(asteroids)):
#             curr_a = asteroids[i]
#             stack_last_i = len(stack) - 1
            
#             if stack:
#                 if (stack[stack_last_i] > 0 and curr_a > 0) or (stack[stack_last_i] < 0 and curr_a < 0):
#                     stack.append(curr_a)
#                 elif stack[stack_last_i] < 0  and curr_a > 0:
#                     stack.append(curr_a)
#                 elif stack[stack_last_i] > 0 and curr_a < 0:
#                     stop = False
#                     curr_stack_i = stack_last_i

#                     while stop == False and curr_stack_i >= 0:
#                         if stack[curr_stack_i] > 0 and curr_a < 0: #collision directions
#                             if abs(stack[curr_stack_i]) < abs(curr_a):
#                                 stack.pop()
#                                 curr_stack_i -= 1
#                             elif abs(stack[curr_stack_i]) == abs(curr_a):
#                                 stack.pop()
#                                 stop = True
#                             else:
#                                 stop = True
#                         else:
#                             stack.append(curr_a)
#                             stop = True

#                     if curr_stack_i < 0:
#                         stack.append(curr_a)
#             else:
#                 stack.append(curr_a)
#         return stack
    
#06/18/24 Attempt 3
# class Solution(object):
#     def asteroidCollision(self, asteroids):
#         """
#         :type asteroids: List[int]
#         :rtype: List[int]
#         """

#         stack = list()
#         stack.append(asteroids[0])

#         for i in range (1, len(asteroids)):
#             curr_a = asteroids[i]
#             stack_last_i = len(stack) - 1
            
#             if stack:
#                 if stack[stack_last_i] > 0 and curr_a < 0:
#                     stop = False
#                     curr_stack_i = stack_last_i

#                     while curr_stack_i >= 0: #stop == False and 
#                         if stack[curr_stack_i] > 0 and curr_a < 0: #collision directions
#                             if abs(stack[curr_stack_i]) < abs(curr_a):
#                                 stack.pop()
#                                 curr_stack_i -= 1
#                             elif abs(stack[curr_stack_i]) == abs(curr_a):
#                                 stack.pop()
#                                 break
#                             else:
#                                 break
#                         else:
#                             stack.append(curr_a)
#                             stop = True

#                     if curr_stack_i < 0:
#                         stack.append(curr_a)
#                 else:
#                     stack.append(curr_a)
#             else:
#                 stack.append(curr_a)

#         return stack
    
#06/18/24 Attempt 4
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = list()
        # stack.append(asteroids[0])

        for i in range (0, len(asteroids)):
            curr_a = asteroids[i]

            while stack and stack[-1] > 0 and curr_a < 0: # conflict
                if stack[-1] < -curr_a:
                    stack.pop()
                elif stack[-1] == -curr_a:
                    stack.pop()
                    break
                else:
                    # stack.append(curr_a)
                    break

            else: #either stack is empty or not a conflict case
                stack.append(curr_a)

        return stack

solution = Solution()
# solution.asteroidCollision([1,-1,-2,-2])
solution.asteroidCollision([5, 10, -5])