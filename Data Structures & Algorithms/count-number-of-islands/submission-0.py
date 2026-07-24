class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #range i, range j
        num_r, num_c = len(grid), len(grid[0])
        num_islands = 0

        def dfs(i,j):
            if i<0 or i>=num_r: return
            if j<0 or j>=num_c: return
            if grid[i][j] == "0": return
            grid[i][j] = "0"
            for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
                dfs(i+x,j+y)

        for i in range(num_r):
            for j in range(num_c):
                if grid[i][j]=="1":
                    num_islands += 1
                    dfs(i,j)
        return num_islands