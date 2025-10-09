class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if (x < 0):
            return False;
        z = str(x);
        
        return self.isStrPalindrome(z);
       
    
    def isStrPalindrome(self, z):
        if (len(z) <= 1):
            return True;
        
        first = z[0];
        last = z[-1];
        
        if (first != last):
            return False;
        
        return self.isStrPalindrome(z[1 : -1]);
        
        