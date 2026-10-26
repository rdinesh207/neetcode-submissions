class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        def dfs(r, c, k, vis):
            if k==len(word):
                return True
            vis.add((r,c))
            print((r,c) in vis, (r,c), vis)
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            for x,y in dirs:
                row = r+x
                col = c+y
                if ((row, col)) in vis:
                    continue
                if row>=0 and col>=0 and row<len(board) and col<len(board[0]) and board[row][col]==word[k]:
                    if dfs(row, col, k+1, vis):
                        return True
            return False
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]==word[0]:
                    if dfs(r,c,1,set()):
                        return True
        return False
                        


        