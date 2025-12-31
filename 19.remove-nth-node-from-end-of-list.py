#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x1 = head
        x0 = None
        y = head

        for i in range(n):
            y = y.next

        while y is not None:
            y = y.next
            x0 = x1
            x1 = x1.next
        if x0 is None:
            return x1.next
        x0.next = x1.next
        x1.next = None

        return head


# @lc code=end
