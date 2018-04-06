# example of stack operation from stack.py

import stack as st

s = st.Stack()

print(s.isEmpty())

s.push(99)
s.push('hello')
print('Peak operation: '+ s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(1.3)

for i in range(s.size()):
    print(s)
