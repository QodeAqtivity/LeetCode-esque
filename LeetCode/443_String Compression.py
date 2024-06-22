#06/12/24 Attempt #2
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        last_index = 0
        s = ''
        prev = None
        count = None

        for i in range(0, len(chars)):
            curr = chars[i]

            if (len(chars) == 1):
                return 1
            # if (i == 0):
            #     prev = curr
            #     count = 1
            #     s += curr
            elif (i == len(chars) - 1):
                if curr == prev:
                    count += 1
                if (count != 1):
                    for j in range(0, len(str(count))):
                                s += str(count)[j]
                if curr != prev:
                    s += curr
                
            elif (curr != prev): #or (i == len(chars) - 1):
                # if (i == len(chars) - 1):
                #     count += 1
 
                count_str = str(count)
                if (i != 0):
                    if count != 1:
                        print(len(str(count)))
                        for j in range(0, len(str(count))):
                            s += str(count)[j]

                prev = curr
                count = 1
                s += curr
            else: #not the last index and is the same char as previous char
                count += 1

        print(s)
        for i in range (0, len(s)):
            chars[i] = s[i]

        for i in range(len(s), len(chars)):
            chars.pop()

        return len(chars)

#06/12/24 Attempt #1
# class Solution(object):
#     def compress(self, chars):
#         """
#         :type chars: List[str]
#         :rtype: int
#         """
        
#         s = ''
#         prev = None
#         count = None

#         for i in range(0, len(chars)):
#             if (len(chars) == 1):
#                 return 1
#             elif (i == 0):
#                 prev = chars[i]
#                 s += chars[i]
#                 count = 1
#             elif (i == len(chars) - 1) or (chars[i] != prev):
                
#                 if i == len(chars) - 1: #last index
#                     count += 1

#                 if count != 1:
#                     thousand = count // 1000
#                     hundred = (count % 1000) // 100
#                     ten = (count % 100) // 10
#                     one = (count % 10)

#                     if thousand:
#                         # s += f'{thousand}'
#                         s += str(thousand)
#                     if hundred:
#                         # s += f'{hundred}'
#                         s += str(hundred)
#                     elif thousand: 
#                         s += str(0)
#                     if ten:
#                         # s += f'{ten}'
#                         s += str(ten)
#                     elif thousand or hundred:
#                         s += str(0)
#                     s += str(one)

#                     prev = chars[i]
#                     s += chars[i]
#                     count = 1
#             else:
#                 count += 1
            
#         print(s)
#         for i in range (0, len(s)):
#             chars[i] = s[i]

#         for i in range(len(s) - 1, len(chars)):
#             chars.pop()

#         return len(chars)


        #     if chars[i] != prev:

        # for char in chars:
        #     if char != prev:
        #         # s += str(prev)
        #         thousand = count // 1000
        #         hundred = (count % 1000) // 100
        #         ten = (count % 100) // 10
        #         one = (count % 10)

        #         if thousand:
        #             # s += f'{thousand}'
        #             s += str(thousand)
        #         if hundred:
        #             # s += f'{hundred}'
        #             s += str(hundred)
        #         if ten:
        #             # s += f'{ten}'
        #             s += str(ten)
        #         # # if (thousand or hundred or ten) and not one:
        #         # if thousand or hundred or ten:
        #         #     # s += '0'
        #         #     s += f'{one}'
        #         # # elif (thousand or hundred or ten) and one:
        #         # elif not (thousand or hundred or ten) and one:
        #         # s += f'{one}'
        #         s += str(one)

        #         prev = char
        #         s += char
        #         count = 1
        #     else:
        #         count += 1
        # print(s)
        # return len(s)
solution = Solution()
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","a","a","a","b"]
solution.compress(chars)