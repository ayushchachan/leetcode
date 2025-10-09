class Solution:
    def merge(self, intervals):
        L = sorted(intervals, key=lambda f : (f[0], f[1]))
        result = [L[0]]

        for i in range(1, len(L)):
            si, fi = L[i]

            if si <= result[-1][1]:
                if fi > result[-1][1]:
                    result[-1][1] = fi
            else:
                result.append(L[i])
        return result