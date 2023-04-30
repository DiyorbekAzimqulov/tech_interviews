class Stack:

    def __init__(self):
        self.elements = []

    def push(self, element):
        """pushes element at the top of the stack"""
        self.elements.append(element)

    def pop(self):
        """removes top element of the stack"""
        return self.elements.pop()
    
    def get_stack(self):
        """returns current state of the stack"""
        return self.elements

    def is_empty(self) -> bool:
        return self.elements == []


wardrobe = Stack()
wardrobe.push('jeans')
wardrobe.push('t-shirt')
wardrobe.push('mayka')
wardrobe.push('shim')
print(wardrobe.get_stack())
wardrobe.pop()
print(wardrobe.get_stack())