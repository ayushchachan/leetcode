class Solution:
    def isPalindrome(self, s: str) -> bool:
        # chars = []
        # for c in s:
        #     if c.isalnum():
        #         chars.append(c.lower())
        # s = "".join(chars)
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


# teststr = "A man, a plan, a canal: Panama"

# S = Solution()
# print(S.isPalindrome(teststr))