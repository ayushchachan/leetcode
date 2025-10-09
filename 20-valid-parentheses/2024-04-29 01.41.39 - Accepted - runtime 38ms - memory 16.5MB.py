class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in ["}", "]", ")"]:
                if len(st) == 0 or d[ch] != st.pop():
                    return False
            else:
                st.append(ch)
        return len(st) == 0