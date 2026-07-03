class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.MinStack=[]
        

    def push(self, value):
        self.stack.append(value)
        if not self.MinStack or value<=self.MinStack[-1]:
            self.MinStack.append(value)
        else:
            self.MinStack.append(self.MinStack[-1])
        

    def pop(self):
        self.stack.pop()
        self.MinStack.pop()


    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.MinStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()