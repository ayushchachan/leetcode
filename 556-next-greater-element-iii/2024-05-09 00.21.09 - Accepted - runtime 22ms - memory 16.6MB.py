#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        if(len(s) > 32):
            return -1
        st = []
        res = ''
        for i in range(len(s) - 1,-1,-1):
            lastEle = None
            while(len(st) != 0  and st[-1][0] > int(s[i])):
                lastEle = st.pop()
            
            if(lastEle == None):
                st.append((int(s[i]),i))
            else:
                temp = int(s[i])
                s[i],s[lastEle[1]] = s[lastEle[1]],s[i]
                res = s[:i + 1] + s[:i:-1]
                res = int(''.join(res))
                return  res if res < 2147483648 else -1
            
        return -1
    

# @lc code=end

