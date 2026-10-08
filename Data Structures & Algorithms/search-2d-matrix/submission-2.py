class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        low,high = 0, m-1
        while low<=high:
            mid = low + (high-low)//2
            if target>matrix[mid][-1]: low = mid+1
            elif target<matrix[mid][0]: high = mid-1
            else: break
        if not(low<=high): return False
        row = low + (high-low)//2
        l,r = 0,n-1
        while l<=r:
            m = l + (r-l)//2
            if matrix[row][m] == target: return True
            if target<matrix[row][m]:
                r = m-1
            else:
                l = m+1
        return False

