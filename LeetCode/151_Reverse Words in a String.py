# 6/11/24 Attempt 2 (alpha)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        word_list = list()
        curr_index = 0
        start_word = False
        end_word = False 
        word = ''

        while (curr_index < len(s)):
            if (s[curr_index].isalpha() and (curr_index == 0 or s[curr_index - 1] == ' ')):
                start_word = True
                word += s[curr_index]
            elif (s[curr_index].isalpha() and (curr_index == len(s) - 1 or s[curr_index + 1] == ' ')):
                end_word = True
                word += s[curr_index]
            elif (s[curr_index].isalpha() and s[curr_index - 1].isalpha() and s[curr_index + 1].isalpha()):
                word += s[curr_index]
            if(not s[curr_index].isalpha() and start_word):
                end_word = True

            if (start_word and end_word):
                start_word = False
                end_word = False

                word_list.append(word)
                word = ''

            curr_index += 1

        for word in word_list:
            print(word)

        sol_str = ''            
        for i in range(len(word_list) - 1, -1, -1): #remove -1 step 
            sol_str += word_list[i] 
            sol_str += ' '

        return sol_str[0:len(sol_str)-1]
            
                
# 6/11/24 Attempt 1 (alphanumeric)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        word_list = list()
        curr_index = 0
        start_word = False
        end_word = False 
        word = ''

        while (curr_index < len(s)):
            if (s[curr_index].isalnum() and (curr_index == 0 or s[curr_index - 1] == ' ')):
                start_word = True
                word += s[curr_index]
            elif (s[curr_index].isalnum() and (curr_index == len(s) - 1 or s[curr_index + 1] == ' ')):
                end_word = True
                word += s[curr_index]
            elif (s[curr_index].isalnum() and s[curr_index - 1].isalnum() and s[curr_index + 1].isalnum()):
                word += s[curr_index]

            if(not s[curr_index].isalnum() and start_word) or (start_word and curr_index == len(s) - 1):
                end_word = True

            if (start_word and end_word):
                start_word = False
                end_word = False

                word_list.append(word)
                word = ''

            curr_index += 1

        sol_str = ''            
        for i in range(len(word_list) - 1, -1, -1): #remove -1 step 
            sol_str += word_list[i] 
            sol_str += ' '

        return sol_str[0:len(sol_str)-1]



# $ src: https://leetcode.com/problems/reverse-words-in-a-string/solutions/5264467/python-beat-95-100-efficient-optimal-solution-easy-to-understand/?envType=study-plan-v2&envId=leetcode-75
#6/11/24 Attempt 2 
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        word_list = s.split()
        reversed = word_list[::-1]
        reversed_string = ' '.join(reversed)
        return reversed_string