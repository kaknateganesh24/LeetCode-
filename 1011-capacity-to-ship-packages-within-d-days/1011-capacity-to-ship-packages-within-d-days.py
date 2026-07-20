class Solution(object):
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        while low<=high:
            capacity=(low+high)//2
            days_needed = 1
            current_load = 0
            for weight in weights:
                if current_load+weight>capacity:
                    days_needed+=1
                    current_load=0
                current_load+=weight
            if days_needed<=days:
                high=capacity-1
            else:
                low=capacity+1
        return low
        