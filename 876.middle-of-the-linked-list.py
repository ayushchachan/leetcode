#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        y = head.next
        while y is not None:
            y = y.next
            if y is not None:
                y = y.next
            x = x.next
        return x


# @lc code=end
