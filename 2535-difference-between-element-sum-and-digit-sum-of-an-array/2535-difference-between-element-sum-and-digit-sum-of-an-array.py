class Solution(object):
    def differenceOfSum(self, nums):
        summation=sum(nums)
        num_digits=0
        for digits in nums:
            for ch in str(digits):
                num_digits+=int(ch)
            difference=summation-num_digits
        return difference