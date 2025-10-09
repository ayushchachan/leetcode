#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        N = len(s)
        count_star = 0
        last_star_index = -1
        last_open_index = -1
        for i in range(N):
            c = s[i]
            if c == "(":
                stack.append(c)
                last_open_index = i
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                elif count_star != 0:
                    count_star -= 1
                else:
                    return False
            else:
                count_star += 1
                last_star_index = i
        if len(stack) == 0:
            return True
        else:
            return last_star_index < last_open_index
        


s = "(((**))("
s1 =Solution()
print(s1.checkValidString(s))


# @lc code=end

