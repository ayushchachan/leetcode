import java.util.PriorityQueue;
import java.util.ArrayList;
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
    public ListNode mergeKLists(ListNode[] lists) {
        
        if (lists.length == 1) return lists[0];
        
        //System.out.println("input = " + java.util.Arrays.deepToString(lists));
        PriorityQueue<IntIndexPair> pq = new PriorityQueue<>();
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i< lists.length; i++) {
            if (lists[i] != null) {
                pq.add(new IntIndexPair(lists[i].val, i));
                lists[i] = lists[i].next;
            }
        }
        
        while (!pq.isEmpty()) {
            //System.out.println("pq before pop = " + pq);
            IntIndexPair x = pq.poll();
            answer.add(x.value);
            
            //System.out.println("pq after pop = " + pq);
            
            int i = x.listIndex;
            
            
            if (lists[i] != null) {
                pq.add(new IntIndexPair(lists[i].val, i));
                lists[i] = lists[i].next;
            }
        }
        
        int N = answer.size();
        
        if (N == 0) return null;
        ListNode ansF = new ListNode(answer.get(N - 1), null);
        for (int j = N - 2; j >= 0; j--) {
            ansF = new ListNode(answer.get(j), ansF);
        }
        return ansF;
    }
    
    public static void main(String[] args) {
        // [[1,4,5],[1,3,4],[2,6]]
        ListNode[] lists = new ListNode[3];
        
        lists[0] = new ListNode(5, null);
        lists[0] = new ListNode(4, lists[0]);
        lists[0] = new ListNode(1, lists[0]);
        
        lists[1] = new ListNode(4, null);
        lists[1] = new ListNode(3, lists[1]);
        lists[1] = new ListNode(1, lists[1]);
        
        lists[2] = new ListNode(6, null);
        lists[2] = new ListNode(2, lists[2]);
        
        Solution s = new Solution();
        s.mergeKLists(lists);
    }
}

class IntIndexPair implements Comparable<IntIndexPair> {
    int value;
    int listIndex;
    
    public IntIndexPair(int a, int b) {
        this.value = a;
        this.listIndex = b;
    }
    
     

    @Override
    public int compareTo(IntIndexPair o) {
        return Integer.compare(this.value, o.value);
    }
    
    public String toString() {
        return "(val = " + this.value + ", index = " + this.listIndex + ")";
    }
    
}
