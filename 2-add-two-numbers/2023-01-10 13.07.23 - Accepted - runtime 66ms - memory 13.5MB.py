# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addList(l1, l2)

    def addList(self, n1, n2, carry = 0):
        a, b = 0, 0
        if not (n1 or n2):
            if carry:
                return ListNode(carry)
            else:
                return None
        if n1:
            a = n1.val
            n1 = n1.next
        if n2:
            b = n2.val
            n2 = n2.next



        if (a + b + carry) < 10:
            result = ListNode(a + b + carry)
            carry = 0
        else:
            result = ListNode(a + b + carry - 10)
            carry = 1

        list2 = self.addList(n1, n2, carry)
        result.next = list2
        return result

