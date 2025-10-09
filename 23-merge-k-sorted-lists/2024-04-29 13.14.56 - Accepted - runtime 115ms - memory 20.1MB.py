# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import queue


class MyELe:
    def __init__(self, node) -> None:
        self.node = node

    def __lt__(self, ele):
        return self.node.val < ele.node.val

    def __gt__(self, ele):
        return self.node.val > ele.node.val

    def __eq__(self, ele):
        return self.node.val == ele.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = queue.PriorityQueue(len(lists))
        head = None;
        tail = None;

        for i in range(len(lists)):
            ele = lists[i]
            if(ele == None):
                continue
            pq.put(MyELe(ele))
        
        while(pq.qsize() > 0):
            temp = pq.get().node
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
            pq.put(MyELe(temp.next)) if temp.next != None else ''

        return head

