class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRS = [[0,1], [0,-1], [1,0], [-1,0]]
        NUM_R, NUM_C = len(grid), len(grid[0])
        rotten_fruits,visited = [],[]
        count_fresh_fruits = 0 

        for i in range(NUM_R):
            for j in range(NUM_C):
                if grid[i][j]==2:
                    rotten_fruits.append((i,j))
                    visited.append((i,j))
                if grid[i][j]==1:
                    count_fresh_fruits += 1

        if count_fresh_fruits and not len(rotten_fruits): return -1
        if not count_fresh_fruits: return 0
        

        def updateRottenFruits(i,j):
            if (i<0 or i>=NUM_R) or (j<0 or j>=NUM_C) or grid[i][j]==0 or (i,j) in visited:
                return
            rotten_fruits.append((i,j))
            visited.append((i,j))
        
        time, count_fresh_to_rotten = -1,0
        while rotten_fruits:
            len_fruits = len(rotten_fruits)
            len_visited = len(visited)
            for _ in range(len_fruits):
                i,j = rotten_fruits.pop(0)
                if grid[i][j]==1: count_fresh_to_rotten += 1
                grid[i][j] = 2
                for x,y in DIRS:
                    updateRottenFruits(i+x,j+y)
            time += 1
        return( time if count_fresh_fruits==count_fresh_to_rotten else -1)