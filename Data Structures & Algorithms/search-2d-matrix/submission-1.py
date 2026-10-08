class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        if target<matrix[0][0]: return False

        i,j = 0,0
        while i<m:
            if matrix[i][-1]==target: return True
            if target<matrix[i][-1]: break
            i += 1
        while i<m and j<n:
            if matrix[i][j]==target: return True
            j+=1
        return False

