#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ## first need to compute length
        temp = 1

        y = x
        while y != 0:
            y = y // 10
            temp = temp * 10

        temp = temp // 10
        print(temp)

        return False


S = Solution()
print(S.isPalindrome(1234))
# @lc code=end
