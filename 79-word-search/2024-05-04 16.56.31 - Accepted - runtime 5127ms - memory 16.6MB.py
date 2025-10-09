

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        currentStack = set()

        def validate(r, c):
            if (r, c) in currentStack:
                return False
            if r < 0 or c < 0:
                return False
            if r >= len(board) or c >= len(board[0]):
                return False
            return True

        def dfs(r, c, k):
            if not validate(r, c) or board[r][c] != word[k]:
                return False

            if board[r][c] == word[k] and k == len(word) - 1:
                return True

            currentStack.add((r, c))

            res = (
                dfs(r - 1, c, k + 1)
                or dfs(r, c + 1, k + 1)
                or dfs(r + 1, c, k + 1)
                or dfs(r, c - 1, k + 1)
            )

            currentStack.remove((r, c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False

