class QuickFind:
    """
    Quick find is a sort of data structure
    which defines two vertices of the graph are connected or not.
    """
    
    roots = []  # stores root vertex of the vertices. element is root vertex, index is the actual vertex

    def __init__(self, size):
        """
        Initializes numbers as root of its own
        """
        # initialize array, right now every element is its own root
        self.roots = [i for i in range(size)]

    def find(self, idx: int) -> int:
        
        """
        Given the index which is the actual vertex, it finds its root and returns it.
        """

        return self.roots[idx]

    def union(self, x: int, y: int) -> None:

        """
        Unions two vertex and assignes first vertex root as head root for both.
        """

        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            for i in range(len(self.roots)):
                if self.roots[i] == y_root:
                    self.roots[i] = x_root
    
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

qf = QuickFind(4)
qf.union(0, 3)
qf.union(1,2)
qf.union(2, 3)
print(qf.roots)
print(qf.connected(1, 0))