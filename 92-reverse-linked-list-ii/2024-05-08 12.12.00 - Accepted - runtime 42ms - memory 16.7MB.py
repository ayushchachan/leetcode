# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        tempNext = temp.next
        beforeNode = None
        tailR = head
        i = 1
        while(i < right):
            if(i < left):
                beforeNode = temp
                temp = temp.next
                tailR = temp
                tempNext = temp.next
            else:
                savenode = tempNext.next
                tempNext.next = temp
                temp = tempNext
                tempNext = savenode
            i += 1

        if(beforeNode == None):
            head = temp
        else:
            beforeNode.next = temp
        
        tailR.next = tempNext

        return head
        
                


        
