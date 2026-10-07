class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        w = len(heights)-1
        maxArea = 0

        while l<r:
            lHeight,rHeight = heights[l], heights[r]
            if lHeight < rHeight:
                h = lHeight
                l += 1
            else:
                h = rHeight
                r -=1
            area = h*w
            w -= 1
            maxArea = max(maxArea, area)
        return maxArea

