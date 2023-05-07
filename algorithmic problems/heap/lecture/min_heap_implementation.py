"""
implementation of a min heap data structure using array. 
complete binary tree is converted to array as follows
index of a parent node of any node is index of a node is divided by 2 and getting result's integer value
parent -> int(node.index / 2)
left child node.index * 2
right child node.index * 2 + 1
is leaf node = > node.index > int(number of elements / 2)

Adding elements to a heap
we insert an element directly and satisfy a complete binary tree condition
then we heapify (satisfy 2-properties of a complete binary tree)

Removing elements from a heap
we put last element of the heap to the top directly
then we heapify(satisfy 2-properties of a complete binary tree)
if left child value is less than right child value parent gets replaced with left child value
"""


class MinHeap:

    def __init__(self, heap_size):
        self.min_heap = [0] * (heap_size + 1)
        self.real_size = 0
        self.heap_size = heap_size

    def add(self, element):
        self.real_size += 1
        if self.real_size > self.heap_size:
            print('we have many elements than storage!')
            self.real_size -= 1
            return

        self.min_heap[self.real_size] = element
        node = self.real_size
        parent = node // 2
        while self.min_heap[node] < self.min_heap[
                parent] and node > 1:  # node is not a root node
            self.min_heap[parent], self.min_heap[node] = self.min_heap[
                node], self.min_heap[parent]
            node = parent
            parent = node // 2

    def remove(self):
        if self.real_size < 1:
            print('can not be removed, it is empty!')
            return
        removed_element = self.min_heap[1]
        self.min_heap[1] = self.min_heap[self.real_size]
        node = 1
        self.real_size -= 1
        while (node <= self.real_size // 2):
            left = node * 2
            right = node * 2 + 1
            if self.min_heap[node] < self.min_heap[left] or self.min_heap[
                    node] < self.min_heap[right]:
                if self.min_heap[left] < self.min_heap[right]:
                    self.min_heap[left], self.min_heap[node] = self.min_heap[
                        node], self.min_heap[left]
                    node = left
                else:
                    self.min_heap[right], self.min_heap[node] = self.min_heap[
                        node], self.min_heap[right]
                    node = right
            else:
                break
        return removed_element


heap = MinHeap(10)
heap.add(4)
heap.add(5)
heap.add(8)
heap.add(2)
heap.add(3)
heap.add(5)
heap.add(9)
heap.add(10)
heap.add(4)
while heap.real_size > 3:
    heap.remove()
print(heap.real_size)
print(heap.min_heap[1])
print()
