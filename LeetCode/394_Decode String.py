#06/17/24 Attempt 1
# class Solution(object):
#     def decodeString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
        
#         stack = list()
#         d = dict()
#         num = False
#         start = True
#         depth = 0
#         sub = ''
#         mult = '1'

#         for c in s:
#             if c.isnumeric():
#                 if not num: #previous char was alpha and current is (first) numeric
#                     d[depth] = [sub, int(mult)]
#                     mult = ''
#                     sub = ''
#                     num = True
#                     depth += 1

#                 mult += c
#             elif c.isalpha():
#                 sub += c
#             elif c == '[':
#                 num = False
#             elif c == ']':
#                 # sub = 
#                 depth -= 1
#                 sub = d[depth][0] *sub * mult
            
            
#06/17/24 Attempt 2                
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = list()
        num = False
        sub = ''
        mult = ''

        for c in s:
            if c.isnumeric():
                if stack.count('[') > 1:
                    mult = ''
                mult += c
            elif c.isalpha():
                sub += c
            elif c == '[':
                stack.append(sub)
                stack.append('[')
                stack.append(mult)
                sub = ''
            elif c == ']':
                # stack.append(sub)
                # while stack[-1] != '[':
                mult = int(stack.pop()) #the multiple/integer
                stack.pop() # the [
                sub *= mult
                # stack[-1] += sub
                sub = stack[-1] + sub
                stack.pop()
                mult = ''

        if stack:
            for e in stack:
                print('count')
                sub = e + sub

        return sub
    
solution = Solution()
# solution.decodeString("3[a]2[bc]")
# solution.decodeString("3[a2[c]]")
solution.decodeString("100[leetcode]")
        # for i in range(len(stack) - 1, -1, -1):
        #     if stack[i].isnumeric():
        #         sub *= stack[i]
        #     elif

        # for c in s:
        #     if c.isnumeric():
        #         mult += c
        #     elif c.isalpha():
        #         sub += c
        #     elif c == '[':
        #         stack.append('[')
        #         stack.append(sub)
        #         stack.append(mult)
        #     elif c == ']':
        #         while stack[-1] != '[':
                    