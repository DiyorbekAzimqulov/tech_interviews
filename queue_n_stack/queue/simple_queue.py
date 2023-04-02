class Queue:

    def __init__(self):
        self.start = 0
        self.data = []

    # is_empty, enqueue, dequeue
    def is_empty(self):
        return self.start >= len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.is_empty():
            self.start += 1

    def display(self):
        if self.is_empty():
            print('queue is empty!')
            return
        for idx in range(self.start, len(self.data)):
            print(self.data[idx], end=' -> ')
        print('\n')


q = Queue()
print(q.is_empty())
q.enqueue(1)
q.enqueue(4)
q.enqueue(0)
q.enqueue(2)
q.enqueue(6)
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()