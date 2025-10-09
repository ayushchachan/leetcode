class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if (not contains_zero(i)) and (not contains_zero(n - i)):
                return [i, n - i]
        return [-1, -1]


def contains_zero(x):
    while x is not 0:
        r = x % 10
        if r == 0:
            return True
        x = x // 10
    return False
        