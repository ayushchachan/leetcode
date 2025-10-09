# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head
        if(pointer1 == None):
            return False
        pointer2 = head.next
        if(pointer2 == None):
            return False
        while True:
            pointer1 = pointer1.next
            if pointer2.next == None:
                return False
            pointer2 = pointer2.next.next
            if pointer2 == None or pointer1 == None:
                return False
            if pointer1 == pointer2:
                return True

