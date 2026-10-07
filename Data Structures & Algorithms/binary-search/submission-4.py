class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start,end):
            if start>end: return -1
            print(f"{start}---{end}")
            mid = start + (end-start)//2
            if target == nums[mid]: return mid
            if target<nums[mid]:
                return binary_search(start,mid-1)
            else:
                return binary_search(mid+1,end)
        return binary_search(0,len(nums)-1)