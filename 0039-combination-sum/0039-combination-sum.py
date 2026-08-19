class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, total):
            # base case
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            # recursive case
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # i (not i+1) because unlimited use allowed
                path.pop()

        backtrack(0, [], 0)
        return res
