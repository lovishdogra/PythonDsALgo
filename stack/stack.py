# It is an abstract data type defined by structure and operations
# Stacks are ordered as LIFO (last in first out)

"""
Operations on stack:
1. stack(): create a new stack that is empty. It needs no parameter and it return empty stack.
2. push(item): adds a new item to the top of stack. It need the item and return nothing.
3. pop(): removes the top item from the stack. It need no parameter and returns the item
4. peek(): returns to the top of stack. It need no parameter and return the item.
5. isEmpty(): to check whether stack is empty or not. It return a boolean value.
6. size(): return the number of items in stack.
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)