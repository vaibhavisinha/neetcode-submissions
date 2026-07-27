class Solution:
    def solve(self, board: List[List[str]]) -> None:
        NUM_R, NUM_C = len(board), len(board[0])
        DIRS = [[0,1],[1,0],[0,-1],[-1,0]]

        def getArea(i,j,isBoundary, visited) -> (bool,set):
            if (i<0 or i>= NUM_R) or (j<0 or j>= NUM_C) or board[i][j]=="X" or (i,j) in visited :
                return ((isBoundary, visited))
            visited.add((i,j))
            if i==0 or j==0 or i==NUM_R-1 or j==NUM_C-1: isBoundary = True

            for x,y in DIRS:
                boundary,nodes = getArea(i+x,j+y,isBoundary,visited)
                isBoundary = boundary or isBoundary
                visited.update(nodes)
            return ((isBoundary, visited))

        for i in range(NUM_R):
            for j in range(NUM_C):
                if board[i][j]=="X": continue

                isBoundary, visited = getArea(i,j,False,set())
                if isBoundary: continue
            
                for x,y in visited:
                    board[x][y] = "X"