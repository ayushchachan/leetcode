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
        x = head
        if x == None:
            return
        y = x.next
        x.next = None

        while y != None:
            temp = y.next
            y.next = x
            x = y
            y = temp
        return x
