class UnionFind:
    """
    root array stores parents of verticies as array elements and its index is actual vertex
    """
    root = []

    def __init__(self, array: list) -> None:
        """
        initializes root array as all numbers' root is its own parent
        """
        self.num_map = self.mapping(array)
        self.root = [i for i in range(len(array))]

    def find(self, x):
        """
        finds root of the given vertex via actively searching parents of the verticies of the given vertex
        """
        while x != self.root[x]:
            x = self.root[x]
        return x

    def mapping(self, array: list):
        map_num = {}
        for i in range(len(array)):
            map_num[array[i]] = i
        return map_num

    def union(self, x, y):
        """
        unions two verticies' roots as one root for both
        """
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.root[y_root] = x_root
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)


numbers = [10, 11, 13, 17, 20, 4, 13, 50]
uf = UnionFind(numbers)
uf.union(uf.num_map[10], uf.num_map[13])
uf.union(uf.num_map[10], uf.num_map[17])
uf.union(uf.num_map[20], uf.num_map[50])
uf.union(uf.num_map[10], uf.num_map[50])
print(uf.connected(uf.num_map[17], uf.num_map[20]))