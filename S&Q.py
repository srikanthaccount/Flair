# push
# pop
# size
# Show
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack)<1:
            return None
        else:
            return self.stack.pop()
    def size(self):
        return len(self.stack)
    def show(self):
        return self.stack
sobj = Stack()
sobj.push(10)
print(sobj.show())
sobj.push(20)
print(sobj.show())
sobj.push(30)
print(sobj.show())
print("Size of stack : ",sobj.size())
print(sobj.pop())
print(sobj.show())
print(sobj.pop())
print(sobj.show())
print(sobj.pop())
print(sobj.show())
print(sobj.pop())


class Que:
    def __init__(self):
        self.que=[]
    def push(self,item):
        self.que.append(item)
    def pop(self):
        if len(self.que)<1:
            return None
        else:
            return self.que.pop(que.index[0])
    def size(self):
        return len(self.que)
obj =Que()
obj.push(10)
obj.push(20)
print(obj.size())
obj.pop(10)
