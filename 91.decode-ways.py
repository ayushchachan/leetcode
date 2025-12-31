#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[-1] = 1
        if s[-1] != "0":
            dp[-2] = 1
        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                continue
            val1 = dp[i + 1]
            val2 = 0
            if int(s[i : i + 2]) <= 26:
                val2 = dp[i + 2]
            dp[i] = val1 + val2
        return dp[0]


S = Solution()
print(S.numDecodings("11106"))

# @lc code=end
