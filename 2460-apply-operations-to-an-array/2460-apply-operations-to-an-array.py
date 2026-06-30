class Solution(object):
    def applyOperations(self, nums):
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
               nums[i-1] *= 2
               nums[i]=0
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range (k,len(nums)):
            nums[i]=0
        return nums