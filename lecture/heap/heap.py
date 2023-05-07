class MinHeap:

    def __init__(self, heap_size):
        self.heap_size = heap_size
        self.heap = [0] * (heap_size + 1)
        self.real_size = 0

    def add(self, element):
        self.real_size += 1

        if self.real_size > self.heap_size:
            print('sorry, you can not add!')
            self.real_size -= 1
            return
        self.heap[self.real_size] = element

        node_idx = self.real_size

        parent_idx = node_idx // 2

        while node_idx > 1 and self.heap[node_idx] <= self.heap[parent_idx]:
            self.heap[parent_idx], self.heap[node_idx] = self.heap[
                node_idx], self.heap[parent_idx]
            node_idx = parent_idx
            parent_idx = node_idx // 2

    def delete(self) -> None:
        if self.real_size < 1:
            print('it is empty itself, sorry!')
            return
        self.heap[1] = self.heap[self.real_size]
        self.real_size -= 1
        node_idx = 1
        while node_idx <= self.real_size // 2:
            left_idx = node_idx * 2
            right_idx = node_idx * 2 + 1
            if self.heap[node_idx] > self.heap[left_idx] or self.heap[
                    node_idx] > self.heap[right_idx]:
                if self.heap[left_idx] < self.heap[right_idx]:
                    self.heap[node_idx], self.heap[left_idx] = self.heap[
                        left_idx], self.heap[node_idx]
                    node_idx = left_idx
                else:
                    self.heap[node_idx], self.heap[right_idx] = self.heap[
                        right_idx], self.heap[node_idx]
                    node_idx = right_idx
            else:
                break


heap = MinHeap(10)
heap.add(10)
heap.add(2)
heap.add(50)
heap.add(1)
heap.add(15)
heap.add(21)
print(heap.heap)
heap.delete()
print(heap.heap)
print('asdfasdf')