from typing import List
"""
BST is a great choice to solve this problem.
if m node exist in right child of a node then the node's value is m+1-th largest value

our tree node will store value and counter which indicate how many nodes exist rooted with this node

1. construct BST from given list of integers
2. 
"""


class MinHeap:

    def __init__(self, heapSize):
        # Create a complete binary tree using an array
        # Then use the binary tree to construct a Heap
        self.heapSize = heapSize
        # the number of elements is needed when instantiating an array
        # heapSize records the size of the array
        self.minheap = [0] * (heapSize + 1)
        # realSize records the number of elements in the Heap
        self.realSize = 0

    # Function to add an element
    def add(self, element):
        self.realSize += 1
        # If the number of elements in the Heap exceeds the preset heapSize
        # print "Added too many elements" and return
        if self.realSize > self.heapSize:
            print("Added too many elements!")
            self.realSize -= 1
            return
        # Add the element into the array
        self.minheap[self.realSize] = element
        # Index of the newly added element
        index = self.realSize
        # Parent node of the newly added element
        # Note if we use an array to represent the complete binary tree
        # and store the root node at index 1
        # index of the parent node of any node is [index of the node / 2]
        # index of the left child node is [index of the node * 2]
        # index of the right child node is [index of the node * 2 + 1]
        parent = index // 2
        # If the newly added element is smaller than its parent node,
        # its value will be exchanged with that of the parent node
        while (self.minheap[index] < self.minheap[parent] and index > 1):
            self.minheap[parent], self.minheap[index] = self.minheap[
                index], self.minheap[parent]
            index = parent
            parent = index // 2

    # Get the top element of the Heap
    def peek(self):
        return self.minheap[1]

    # Delete the top element of the Heap
    def pop(self):
        # If the number of elements in the current Heap is 0,
        # print "Don't have any elements" and return a default value
        if self.realSize < 1:
            print("Don't have any element!")
            return sys.maxsize
        else:
            # When there are still elements in the Heap
            # self.realSize >= 1
            removeElement = self.minheap[1]
            # Put the last element in the Heap to the top of Heap
            self.minheap[1] = self.minheap[self.realSize]
            self.realSize -= 1
            index = 1
            # When the deleted element is not a leaf node
            while (index <= self.realSize // 2):
                # the left child of the deleted element
                left = index * 2
                # the right child of the deleted element
                right = (index * 2) + 1
                # If the deleted element is larger than the left or right child
                # its value needs to be exchanged with the smaller value
                # of the left and right child
                if (self.minheap[index] > self.minheap[left]
                        or self.minheap[index] > self.minheap[right]):
                    if self.minheap[left] < self.minheap[right]:
                        self.minheap[left], self.minheap[index] = self.minheap[
                            index], self.minheap[left]
                        index = left
                    else:
                        self.minheap[right], self.minheap[
                            index] = self.minheap[index], self.minheap[right]
                        index = right
                else:
                    break
            return removeElement

    # return the number of elements in the Heap
    def size(self):
        return self.realSize

    def __str__(self):
        return str(self.minheap[1:self.realSize + 1])


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = MinHeap(len(nums))
        for num in nums:
            self.heap.add(num)
        while self.heap.realSize > self.k:
            self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.heapSize += 1
        self.heap.minheap.append(0)
        self.heap.add(val)

        if self.heap.realSize > self.k:
            self.heap.pop()

        print(self.heap.minheap)
        return self.heap.minheap[1]
        # self.heap.add(val)
        # if self.heap.real_size > self.k:
        #     self.heap.remove()

        # return self.heap.min_heap[1]


nums = [4, 5, 8, 2]
k = 3
# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k, nums)
print("return->", obj.add(3))
print("size->", obj.heap.realSize)
print("return->", obj.add(5))
print("size->", obj.heap.realSize)
print("return->", obj.add(10))
print("size->", obj.heap.realSize)
print("return->", obj.add(9))
print("size->", obj.heap.realSize)

print("return->", obj.add(4))
print("size->", obj.heap.realSize)

# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# h = MinHeap(10)
# h.add(4)
# h.add(5)
# h.add(8)
# h.add(2)
# h.add(3)
# h.add(5)
# h.add(10)
# while h.real_size > 3:
#     h.remove()
# print(h.real_size)
# print(h.min_heap)
