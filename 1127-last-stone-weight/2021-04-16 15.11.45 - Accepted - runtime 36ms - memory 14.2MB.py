class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        L = stones.copy();
        
        h = MaxHeap(L);
        while (h.size() >= 2):
            x = h.extractMax();
            y = h.extractMax();
            
            if (x != y):
                h.insert(abs(x - y));
        if (h.isEmpty()):
            return 0;
        else:
            return h.extractMax();
        
class MaxHeap:
    def __init__(self, inList):
        self.A = inList;
        self.heapsize = len(inList);
        self.buildHeap();
        
    
    def size(self):
        return self.heapsize;
    def isEmpty(self):
        return self.heapsize == 0;
    
    def heapify(self, i):
        '''
        Assumes that A[i] does not follow max-heap property
        '''
        l = LEFT(i);
        r = RIGHT(i);
        
        if (l < self.heapsize and self.A[l] > self.A[i]):
            largest = l;
        else:
            largest = i;
            
        if (r < self.heapsize and self.A[r] > self.A[largest]):
            largest = r;
            
        if (largest != i):
            self.A[i], self.A[largest] = self.A[largest], self.A[i];
            self.heapify(largest);
            
    def buildHeap(self):
        for i in range(PARENT(self.heapsize - 1), -1, -1):
            self.heapify(i);
    
    def __str__(self):
        return str(self.A[:self.heapsize]);

    def extractMax(self):
        if (self.heapsize > 0):
            self.A[0], self.A[self.heapsize - 1] = self.A[self.heapsize - 1], self.A[0];
            self.heapsize -= 1;
            self.heapify(0);
            return self.A[self.heapsize]
    
    def insert(self, x):
        self.A[self.heapsize] = x;
        
        p = PARENT(self.heapsize);
        c = self.heapsize;
        while (p >= 0 and self.A[p] < self.A[c]):
            self.A[p], self.A[c] = self.A[c], self.A[p];
            c = p;
            p = PARENT(c)
            
        
        self.heapsize += 1;   

def PARENT(i):
    return (i - 1)//2;

def LEFT(i):
    return 2*i + 1;

def RIGHT(i):
    return 2*i + 2;