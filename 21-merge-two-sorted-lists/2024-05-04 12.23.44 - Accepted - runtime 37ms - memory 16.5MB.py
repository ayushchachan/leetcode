# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1;j = list2
        if(i == None):
            return j
        if(j == None):
            return i
        if(i.val < j.val):
            head = list1
            curr = list1
            i = i.next
        else:
            head = list2
            curr = list2
            j = j.next

        while(True):
            if(i == None and j == None):
                return head
            if(i == None):
                curr.next = j
                j = j.next
            elif(j == None):
                curr.next = i
                i = i.next
            else:
                if(i.val < j.val):
                    curr.next = i
                    i = i.next
                else:
                    curr.next = j
                    j = j.next
            
            curr = curr.next
        return head
                        
        