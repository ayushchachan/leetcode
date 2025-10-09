import java.util.ArrayList;
import java.util.TreeMap;
import java.util.List;
import java.util.LinkedList;







class Pair<K, V> {
    
    private K key;
    private V value;
    
    public Pair(K k, V v) {
        this.key = k;
        this.value = v;
    }
    
    
    public K getKey() {
        return this.key;
    }

    
    public V getValue() {
        return this.value;
    }

   
    public V setValue(V value) {
        V old = this.value;
        this.value = value;
        return old;
    }
}



class Solution {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        TreeMap<Integer, TreeMap<Integer, ArrayList<Integer>>> column_row_map = new TreeMap<>();
        
        Coordinate c = new Coordinate(0, 0);
        LinkedList<Pair<TreeNode, Coordinate>> Q = new LinkedList<>();
        
        TreeNode x = root;
        Q.add(new Pair<>(x, c));
        
        while (!Q.isEmpty()) {
            Pair<TreeNode, Coordinate> p = Q.removeFirst();
            
            TreeNode z = p.getKey();
            Coordinate cZ = p.getValue();
            
            if (z.left != null) {
                Coordinate cL = new Coordinate(cZ.getRow() + 1, cZ.getColumn() - 1);
                Q.add(new Pair<>(z.left, cL));
            }
            
            if (z.right != null) {
                Coordinate cR = new Coordinate(cZ.getRow() + 1, cZ.getColumn() + 1);
                Q.add(new Pair<>(z.right, cR));
            }
            
            if (column_row_map.containsKey(cZ.getColumn())) {
                TreeMap<Integer, ArrayList<Integer>> row_map = column_row_map.get(cZ.getColumn());
                
                if (row_map.containsKey(cZ.getRow())) 
                    row_map.get(cZ.getRow()).add(z.val);
                else {
                    ArrayList<Integer> newList = new ArrayList<>();
                    newList.add(z.val);
                    row_map.put(cZ.getRow(), newList);
                }                   
            } else {
                TreeMap<Integer, ArrayList<Integer>> new_row_map = new TreeMap<>();
                ArrayList<Integer> newList = new ArrayList<>();
                newList.add(z.val);
                new_row_map.put(cZ.getRow(), newList);
                column_row_map.put(cZ.getColumn(), new_row_map);
            }
        }
        
        ArrayList<List<Integer>> answer = new ArrayList<>();
        for (int col : column_row_map.keySet()) {
            
            ArrayList<Integer> col_data = new ArrayList<>();
            for (int row : column_row_map.get(col).keySet()) {
                if (column_row_map.get(col).get(row).size() > 1)
                    column_row_map.get(col).get(row).sort(null);
                col_data.addAll(column_row_map.get(col).get(row));
            }
            answer.add(col_data);
        }
        return answer;
    }
}

class Coordinate {
    
    private int r;
    private int c;
    
    public Coordinate(int r, int c) {
        this.r = r;
        this.c = c;
    }
    
    public Integer getRow() {return this.r;}
    
    public Integer getColumn() {return this.c;}
}

