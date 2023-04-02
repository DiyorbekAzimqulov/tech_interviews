from .queue import MyQueue
from .stack import MyStack


def reverseK(queue, k):
    # Write your code here
    if k > queue.size() or k < 0 or queue.is_empty():
        return None
    stack = MyStack()
    q = MyQueue()
    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        q.enqueue(stack.pop())

    while queue.is_empty() is False:
        q.enqueue(queue.dequeue())
    return q
