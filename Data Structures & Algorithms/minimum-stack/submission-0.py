class MinStack:
    # as we are filling the stack , we will keep record of min val from start .
    # to be able to do it in constant time . we will not keep min val an integer becoz for that we will need to do a O(n) 
    # to find new min if an element is removed , so keeping stack with record of min-value with every push is O(1) 
    def __init__(self):
        self.arr = []
        self.minStack = []


    def push(self, val: int) -> None:
        self.arr.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val) 
        self.minStack.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return  self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


       
        
