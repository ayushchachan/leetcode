/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode x = head, y = head.next;

        while (y != null) {
            x = x.next;
            y = y.next;
            if (y != null)    y = y.next;
            
        } 
        return x;

    }
}