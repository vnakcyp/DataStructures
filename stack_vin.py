class Stack:
    def __init__(self):
        self.stack = []
    def push(self ,val):
        self.stack.append(val)
    def pop(self):
        val = self.stack.pop(len(self.stack) -1)
        return val
class Queue:
    qLen = 5
    def __init__(self):
        self.queue = []
    def enqueue(self, val):
        self.qLen = len(self.queue)
        if(self.qLen == 5):
            print("Queue limit reached \n")
            self.queue.remove(self.queue[self.qLen - 1])
            self.queue.insert(0,val)           
            
        else:
            self.queue.insert(0, val)
    def dequeue(self):       
        return self.queue.pop(len(self.queue) -1)


myStack = Stack()
for i in range(5):
    myStack.push(i)
for i in range(3):
    print(myStack.pop())
myQueue = Queue()
for i in range(8):
    myQueue.enqueue(i)
for i in range(5):
    print(myQueue.dequeue())

