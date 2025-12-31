lookup = dict()


def isSubsetWithSum(arr, n, sumVal):
    if sumVal == 0:
        return True
    if n == 0:
        return False
    if n == 1:
        return arr[0] == sumVal
    if (n - 1, sumVal) in lookup:
        val1 = lookup[(n - 1, sumVal)]
    else:
        val1 = isSubsetWithSum(arr, n - 1, sumVal)
        lookup[(n - 1, sumVal)] = val1

    if (n - 1, sumVal - arr[n - 1]) in lookup:
        val2 = lookup[(n - 1, sumVal - arr[n - 1])]
    else:
        val2 = isSubsetWithSum(arr, n - 1, sumVal - arr[n - 1])
        lookup[(n - 1, sumVal - arr[n - 1])] = val2

    lookup[(n, sumVal)] = val1 or val2
    return val1 or val2


class Solution:
    def isSubsetSum(self, arr, val):
        return isSubsetWithSum(arr, len(arr), val)


S = Solution()
arr = [6, 1, 2, 3, 3, 6]
val = 11
print(S.isSubsetSum(arr, val))
