#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        N = 0

        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)

        y = x
        while y != 0:
            y = y // 10
            N += 1
        ## now we have length of integer
        y = x

        reverse_x = 0
        const = 10 ** (N - 1)
        while y != 0:
            # print(y)
            reverse_x += (y % 10) * const
            y = y // 10
            const = const // 10
        if is_negative:
            return -reverse_x
        return reverse_x


S = Solution()
print(S.reverse(-1234))


# @lc code=end
