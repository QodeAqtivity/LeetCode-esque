#Leetcode 75

#06/21/2024 Attempt 1
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head == None or head.next == None:
            return None

        # floor division
        # SLL therefore we need a prev to keep track of the node behind mid
        end = head
        mid = head
        end_i = 0
        prev = mid
        while end != None:
            # if end_i % 2 == 0: # the end index (currently) is 
            #because of 0 indexing, the parity of the length and cardinality/count of the elements is opposite of its indexing equivalent (0th index vs 1st element)
            if end_i % 2 == 1: # odd index therfore even-numbered element
                prev = mid
                mid = mid.next
            end = end.next
            end_i += 1
        
        prev.next = mid.next

        return head
    
#06/20/2024 Attempt #2
# res: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/solutions/4705282/simple-beginner-friendly-dry-run-two-pointer-approach-time-o-n-space-o-1-gits/?envType=study-plan-v2&envId=leetcode-75
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head == None:
            return None

        prev = ListNode(0)
        prev.next = head 
        mid = prev # mid and end are always/consistent in relative distance from each other because end moves at twice the speed of mid, but setting mid one before where end starts allows for us to access the node one previous from the middle node (deletion node)
        #we don't need the node for deletion to delete it, rather the one prior
        end = head

        while end != None and end.next != None: #currently at a node and there is a node that comes after (to allow for the double stepping for end)
            mid = mid.next 
            end = end.next.next
            # mid increments at half the speed of end

        mid.next = mid.next.next

        # return head ...? why doesnt this work but prev.next works?
        return prev.next