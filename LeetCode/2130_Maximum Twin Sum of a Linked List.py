# LeetCode 75

#06/20/2024 Attempt 1
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        # (Singly) Linked List is even length
        # 0-indexed
        # twin of ith node is (n - 1 - i)th node if 0 <= i <= (n / 2)
        ## equidistant nodes from their respective ends

#         vals = list()
#         sol = 0
#         curr = head
#         i = 0

#         while curr != None:
#             vals.append(curr.val)
#             # vals[i] = curr.val
#             curr = curr.next    
#             i += 1            

#         #the last i += 1 is an overshoot therefore i == n at the end
#         bottom = vals[0:int(i/2)]
#         top = vals[int(i/2):i]
#         top.reverse()

#         # if (len(bottom) == len(top)):
#         #     print('yay')

#         for j in range (0, len(bottom)):
#             if bottom[j] + top[j] > sol:
#                 sol = bottom[j] + top[j]

#         return sol


#06/21/2024 Attempt #1 
#res: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/solutions/3533853/python-java-c-two-pointer-solution/?envType=study-plan-v2&envId=leetcode-75
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        # (Singly) Linked List is even length
        # 0-indexed
        # twin of ith node is (n - 1 - i)th node if 0 <= i <= (n / 2)
        ## equidistant nodes from their respective ends

        #let's formulate 2 SLL
        ## one traversal  O(n)
        ### two halves
        #guaranteed to be even
        # dummy = ListNode(0)
        # dummy.next = head
        # slow = dummy
        # fast = dummy
        # prev = dummy

        # while fast.next != None: #guaranteed to be even
        #     temp = slow
        #     slow = slow.next
        #     fast = fast.next.next
        #     temp.next = prev
        #     prev = temp

        slow = head
        fast = head
        prev = None

        # while fast.next != None:
        # while fast != None and fast.next != None:
        while fast != None: 
            temp = slow
            slow = slow.next
            fast = fast.next.next
            temp.next = prev
            prev = temp

        sol = 0
        while prev != None and slow != None:
            sol = max(sol, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return sol



solution = Solution()
head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
solution.pairSum(head)
