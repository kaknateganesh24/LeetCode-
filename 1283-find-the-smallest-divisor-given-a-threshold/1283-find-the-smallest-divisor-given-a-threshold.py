class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            divisor=0
            for num in nums:
                divisor+=(num+mid-1)//mid
            if divisor<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low