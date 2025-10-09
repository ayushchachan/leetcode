class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        S = set()
        incoming = dict()
        for i in range(1, n + 1):
            S.add(i)
            incoming[i] = []



        for u, v in trust:
            if v not in incoming:
                incoming[v] = []
            incoming[v].append(u)

            if u in S:
                S.remove(u)

        if len(S) == 1:
            judge = S.pop()
            if len(incoming[judge]) == n - 1:
                return judge
        return -1
        
