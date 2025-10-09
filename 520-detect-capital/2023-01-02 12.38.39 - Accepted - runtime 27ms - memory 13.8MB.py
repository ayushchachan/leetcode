class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        countCapital = 0
        for c in word:
            if not c.islower():
                countCapital += 1
        if countCapital in {0, len(word)}:
            return True
        elif countCapital == 1 and not word[0].islower():
            return True
        return False
