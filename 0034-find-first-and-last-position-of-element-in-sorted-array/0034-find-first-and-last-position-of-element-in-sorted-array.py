class Solution(object):
    def findright(self, nums, target):
        low=0
        high=len(nums)-1
        result_index=-1
        while low <=high:
            mid=(low+high)//2
            if nums[mid]==target:
                result_index=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return result_index
    def findLeft(self, nums, target):
        low = 0
        high = len(nums) - 1
        result_index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                result_index = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result_index
    def searchRange(self,nums,target):
        left=self.findLeft(nums,target)
        right=self.findright(nums,target)
        return [left,right]