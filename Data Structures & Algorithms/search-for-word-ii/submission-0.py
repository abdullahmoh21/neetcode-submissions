class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node["$"] = True    # Mark word ending here

        res = []
        def dfs(i, j, s, node):
            if board[i][j] not in node:
                return

            backup = board[i][j]
            child = node[backup]

            if "$" in child:
                res.append(s + backup)
                del child["$"]    # Unmark so the same word can't be added again

            board[i][j] = "#"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = i + dr, j + dc

                if not (0 <= nr < len(board) and 0 <= nc < len(board[0])) or board[nr][nc] == "#":
                    continue

                dfs(nr, nc, s + backup, child)

            board[i][j] = backup

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "", root)

        return res