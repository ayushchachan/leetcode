#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
import math


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        T = haystack
        P = needle

        if len(T) < len(P):
            return -1

        base = 31
        mod = 10**9 + 7
        base_power = pow(31, len(P) - 1, mod)

        hash_p = 0
        for i in range(len(P)):
            hash_p = ((base * hash_p) + ord(P[i])) % mod

        hash_t = 0
        for i in range(len(P)):
            hash_t = ((base * hash_t) + ord(T[i])) % mod

        # print("hash_p =", hash_p)
        # print("hash_t =", hash_t)

        i = 0
        if (hash_t == hash_p) and (P == T[i : i + len(P)]):
            return i
        while i < (len(T) - len(P)):
            # print("i =", i)

            # print("removing T[i] =", T[i])
            # print("adding T[i + len(P)] =", T[i + len(P)])
            hash_t = (
                (hash_t - (ord(T[i]) * base_power) % mod + mod) * base
                + ord(T[i + len(P)])
            ) % mod

            # print("hash_p =", hash_p)
            # print("hash_t =", hash_t)
            i += 1
            if (hash_t == hash_p) and (P == T[i : i + len(P)]):
                return i
        return -1


# T = "ababaabbbbababbaabaaabaabbaaaabbabaabbbbbbabbaabbabbbabbbbbaaabaababbbaabbbabbbaabbbbaaabbababbabbbabaaabbaabbabababbbaaaaaaababbabaababaabbbbaaabbbabb"
# P = "abbbbababbaabaa"
# T = "leetcode"
# P = "tco"

# S = Solution()
# print(S.strStr(T, P))

# @lc code=end
