class MaxHeap:

    def __init__(self, heap_size):
        self.heap_size = heap_size
        self.max_heap = [0] * (heap_size + 1)
        self.real_size = 0

    def add(self, element):
        self.real_size += 1
        if self.real_size > self.heap_size:
            print('can not insert anymore!')
            self.real_size -= 1
            return

        self.max_heap[self.real_size] = element
        node = self.real_size

        parent = node // 2

        while self.max_heap[node] > self.max_heap[parent] and node > 1:
            self.heap_size[parent], self.heap_size[node] = self.heap_size[
                node], self.heap_size[parent]
            node = parent
            parent = node // 2

    def pop(self):
        if self.real_size < 1:
            print('can not delete, because it is empty')
            return
        removed_element = self.max_heap[1]
        self.max_heap[1] = self.max_heap[self.real_size]
        self.real_size -= 1
        node = 1
        while (node <= self.real_size // 2):
            left = node * 2
            right = node * 2 + 1
            if self.max_heap[node] < self.max_heap[left] or self.max_heap[
                    node] < self.max_heap[right]:
                if self.max_heap[left] > self.max_heap[right]:
                    self.max_heap[node], self.max_heap[left] = self.max_heap[
                        left], self.max_heap[node]
                    node = left
                else:
                    self.max_heap[node], self.max_heap[right] = self.max_heap[
                        right], self.max_heap[node]
                    node = right
            else:
                break
        return removed_element


heap = MaxHeap(10)
heap.add(15)
heap.add(1)
heap.add(12)
heap.pop()
print(heap.real_size)
print(heap.max_heap)