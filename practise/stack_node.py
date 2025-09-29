class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.length = 0

  def push(self,item):
    node = Node(item)
    node.next = self.top
    self.top = node
    self.length += 1

  def pop(self):
    if self.isEmpty():
      return None
    data = self.top.data
    self.top = self.top.next
    self.length -= 1
    return data
  
  def peek(self):
    if self.isEmpty():
      return None
    return self.top.data
  

  def isEmpty(self):
    return self.length == 0
  
  def size(self):
    return self.length
  
#Example usage:
myStack = Stack()

myStack.push(1)
myStack.push(2) 
myStack.push(36940)
myStack.push(0)
myStack.push(-5)

print(myStack.size())
print(myStack.peek())

myStack.pop()

print(myStack.size())
print(myStack.peek())
    

  
  
