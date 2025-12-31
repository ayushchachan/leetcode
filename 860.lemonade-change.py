#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
from xmlrpc.client import FastMarshaller


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5 = 0
        change10 = 0

        for bill in bills:

            if bill == 5:
                change5 += 1

            elif bill == 10:
                if change5 == 0:
                    return False
                change5 -= 1
                change10 += 1

            else:
                if change5 == 0:
                    return False
                elif change10 == 0 and change5 < 3:
                    return False
                if change10 == 0:
                    change5 -= 3
                else:
                    change5 -= 1
                    change10 -= 1

        return True


# @lc code=end
