import collections
stack=collections.deque()
stack.append(10)
stack.append(10)
stack.append(10)
stack.append(10)

# print(stack)
# stack.pop()
# print(stack)
import queue
stack=queue.LifoQueue(1)
stack.put(10)
stack.put(20)
