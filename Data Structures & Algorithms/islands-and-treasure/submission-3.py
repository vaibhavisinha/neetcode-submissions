class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        NUM_R, NUM_C = len(grid), len(grid[0])
        # LAND_CELL = 2147483647
        DIRS = [[0,1],[1,0],[0,-1],[-1,0]]
        treasure_chests = []
        visited = []
        for i in range(NUM_R):
            for j in range(NUM_C):
                if grid[i][j]==0:
                    treasure_chests.append((i,j))
                    visited.append((i,j))
        if len(treasure_chests)==0: return grid
        def updateChest(i,j):
            if (i<0 or i>=NUM_R) or (j<0 or j>=NUM_C) or grid[i][j]== -1 or (i,j) in visited:
                return
            visited.append((i,j))
            treasure_chests.append((i,j))

        dist = 0
        while treasure_chests:
            len_dist = len(treasure_chests)
            for _ in range(len_dist):
                i,j = treasure_chests.pop(0)
                grid[i][j] = dist
                for x,y in DIRS:
                    updateChest(i+x,j+y)
            dist += 1