class Solution(object):
    def totalFruit(self, fruits):
        seen={}
        left=0
        max_length=0
        for right in range (len(fruits)):
            fruit=fruits[right]
            seen[fruit]=seen.get(fruit,0)+1
            while len(seen)>2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length