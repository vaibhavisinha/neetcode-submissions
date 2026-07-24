class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_r,num_c = len(grid), len(grid[0])
        max_area = 0

        def get_area(i,j,area):
            if i<0 or i>=num_r: return area
            if j<0 or j>=num_c: return area
            if grid[i][j] == 0: return area

            grid[i][j]=0
            area +=1
            for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
                area = get_area(x+i,y+j,area)
            return area
        
        for i in range(num_r):
            for j in range(num_c):
                if grid[i][j]==1:
                    area = get_area(i,j,0)
                    if area>max_area: max_area = area
        return max_area