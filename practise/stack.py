from collections import deque

class Stack:
    def __init__(self):
        self._stack = deque()

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def is_empty(self):
        return not bool(len(self._stack))

    def size(self):
        return len(self._stack)