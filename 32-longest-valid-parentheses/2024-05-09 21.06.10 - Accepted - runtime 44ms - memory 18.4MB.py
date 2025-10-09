class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        st = []
        resA = [False] * len(s)
        for i in range(len(s)):
            ch = s[i]
            if(ch  == "("):
                st.append((1,i))
            elif(ch == ")"):
                if(len(st) != 0 and st[-1][0] == 1):
                    ele = st.pop()
                    resA[ele[1]] = True
                    resA[i] = True
                else:
                    st.append((-1,i))
        
        
        maxLength = 0
        i = 0
        j = 0 
        while(True):
            ##Check for i
            while(resA[i] != True):
                i += 1
                if(i >= len(resA)):
                    return maxLength
            j = i
            while(resA[j] == True):
                maxLength = max(maxLength,j - i + 1)
                j += 1
                if(j >= len(resA)):
                    return maxLength
            i = j

        