class Solution(object):
    def calPoints(self, ops):
        stack=[]
        for ch in ops:
            if ch=="C":
                stack.pop()
            elif ch=="D":
                D=stack[-1]*2
                stack.append(D)
            elif ch=="+":
                total=stack[-1]+stack[-2]
                stack.append(total)
            else:
                stack.append(int(ch))
        return sum(stack)
