/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.util.PriorityQueue;
import java.util.Comparator;
/**
 *
 * @author Ayush Chachan
 */
public class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        
        for (int i : stones) {
            pq.add(i);
        }
        //System.out.println(pq);
        while (pq.size() >= 2) {
            int x = pq.poll();
            int y = pq.poll();
            
            if (x != y) pq.add(Math.abs(x - y));
        }
        if (pq.isEmpty()) return 0;
        else
            
            return pq.poll();
    }
    
    
}




