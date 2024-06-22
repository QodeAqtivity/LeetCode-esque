#6/18/2024 Attempt 1
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fore = head
        curr = head
        prev = curr

        if not head:
            return None
        elif head.next == None:
            return head

        while curr != None:
        
            if curr.next != None: #not at the end/new head of the SLL
                fore = curr.next

                if prev == curr: #only at old head
                    curr.next = None
                else:
                    curr.next = prev

                prev = curr
                curr = fore
            else:
                head = curr
                curr.next = prev
                curr = None

        return head

#6/18/2024 Attempt 2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fore = head
        curr = head
        prev = None

        # if not head:
        #     return None
        # elif head.next == None:
        #     return head

        while curr != None:
        
            if curr.next != None: #not at the end/new head of the SLL
                fore = curr.next
                curr.next = prev
                prev = curr
                curr = fore
            else:
                head = curr
                curr.next = prev
                curr = None

        return head
