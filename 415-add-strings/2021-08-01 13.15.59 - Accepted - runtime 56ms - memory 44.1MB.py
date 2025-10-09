class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if (not num1):
            return num2;
        if (not num2):
            return num1;
        
        new1 = num1[0:-1];
        new2 = num2[0:-1];
        
        suffix = str(int(num1[-1]) + int(num2[-1]));
        
        if len(suffix) > 1:
            return self.addStrings(self.addStrings(new1, new2), suffix[0]) + suffix[-1];
        
        else:
            return self.addStrings(new1, new2) + str(suffix);
        