# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def oddEvenList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
        
#         # traversing SLL O(n)
#         # individually finding the proper place, either reassigning 'val' or repointing, O(n) [because of individual traversing/backtracking]\
#         # using 2 seperate lists for even and odd would be O(n) extra space complexity

#         curr = head
        
        
#         if curr == None or curr.next == None or curr.next.next == None:
#             return curr

#         curr = curr.next.next #3rd node
#         counter = 3
#         c_even = head.next #2nd node
#         odd_val = curr.val

#         while curr != None:
#             if counter % 2 == 0:
#                 c_even = curr
#                 # c_even.val = odd_val
#             else:
#                 c_even.val = curr.val
#                 # odd_val = curr.val
#             curr = curr.next
#             counter += 1

#         return head
            

# class Solution(object):
#     def oddEvenList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
        
#         # traversing SLL O(n)
#         # individually finding the proper place, either reassigning 'val' or repointing, O(n) [because of individual traversing/backtracking]\
#         # using 2 seperate lists for even and odd would be O(n) extra space complexity

#         curr = head
        
        
#         if curr == None or curr.next == None or curr.next.next == None:
#             return curr

#         curr = curr.next.next #3rd node
#         counter = 3
#         c_even = head.next #2nd node
#         odd_val = curr.val

#         while curr != None:
#             if counter % 2 == 0:
#                 c_even = curr
#                 # c_even.val = odd_val
#             else:
#                 c_even.val = curr.val
#                 c_even = curr
#                 # odd_val = curr.val
#             curr = curr.next
#             counter += 1

#         return head
            
#06/20/24 (Sucessful) Attempt #1 
#res: https://leetcode.com/problems/odd-even-linked-list/solutions/5275264/best-solution-with-explanation-beats-100/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        odd_dummy = ListNode(0)
        even_dummy = ListNode(0)
        odd_ptr = odd_dummy
        even_ptr = even_dummy

        i = 1 # starts at 1

        curr = head

        while curr != None:
            if i % 2 == 1: # odd
                odd_ptr.next = curr
                odd_ptr = odd_ptr.next # curr
            else: # even ,,, (i % 2 == 0)
                even_ptr.next = curr
                even_ptr = even_ptr.next #curr

            curr = curr.next
            i += 1

        odd_ptr.next = even_dummy.next
        even_ptr.next = None
        return odd_dummy.next 