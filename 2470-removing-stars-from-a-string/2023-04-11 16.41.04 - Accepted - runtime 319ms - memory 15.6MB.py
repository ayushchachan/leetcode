class Solution:
    def removeStars(self, s: str) -> str:
        S = []

        for i in range(len(s)):
            c = s[i]
            if c != '*':
                S.append(c)
            else:
                if not S:
                    raise Exception("Bad String s")
                S.pop()
                continue
        return "".join(S)