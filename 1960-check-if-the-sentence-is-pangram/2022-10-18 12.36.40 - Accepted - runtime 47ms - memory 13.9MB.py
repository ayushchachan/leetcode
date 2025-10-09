class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        import string
        all_alphabets = set(string.ascii_lowercase)
        for c in sentence:
            if c in all_alphabets:
                all_alphabets.remove(c)
        if all_alphabets:
            return False
        return True