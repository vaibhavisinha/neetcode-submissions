class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m = (r-l)//2+l
            if target==nums[m]: return m
            if target<nums[m]:
                r = m-1
            else:
                l = m+1
        return -1
        # def binary_search(start,end):
        #     if start>end: return -1
        #     print(f"{start}---{end}")
        #     mid = start + (end-start)//2
        #     if target == nums[mid]: return mid
        #     if target<nums[mid]:
        #         return binary_search(start,mid-1)
        #     else:
        #         return binary_search(mid+1,end)
        # return binary_search(0,len(nums)-1)