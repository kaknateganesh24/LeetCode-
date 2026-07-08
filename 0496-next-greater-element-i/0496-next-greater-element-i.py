class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        result={}
        for i in range (len(nums2)):
            current=nums2[i]
            while stack and current>stack[-1]:
                popped=stack.pop()
                result[popped]=current
            stack.append(current)
        for num in stack:
            result[num]=-1
        final_answer=[]
        for num in nums1:
            final_answer.append(result[num])
        return final_answer