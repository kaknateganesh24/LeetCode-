class Solution(object):
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        while low<=high:
            k=(low+high)//2
            total_hours = 0 
            for pile in piles:
                total_hours += (pile + k - 1) // k
            if total_hours<=h:
                high=k-1
            else:
                low=k+1
        return low

        