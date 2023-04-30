"""
Union by rank is more optimal solution when merging two separated graph:
First of all, calculating both rank and taking the one which has higher rank and making its root as ultimate root for both head.
        1
       /   \   if we were to connect 3->3, we do it by calculating rank of both separated nodes and choosing the node as root    
       3    3    with higher rank, we connect 1->3 instead of 3->

"""


class UnionRank:

    parent = []
    mapping = dict()


    def __init__(self, numbers: list) -> None:
        self.rank = [1 for i in range(len(numbers))]
        self.parent = [i for i in range(len(numbers))]
        self.mapping = {}
        for i in range(len(numbers)):
            self.mapping[numbers[i]] = i
    

    def optimized_find(self, num):
        """it finds the root of the vertex"""

        if num == self.parent(num):
            return num
        self.parent[num] = self.optimized_find(self.parent[num])
        return self.parent[num]


    def union(self, x, y):
        """
        unions two verticies' root node as one by their rank
        """
        xroot = self.find(self.mapping[x])
        yroot = self.find(self.mapping[y])
        if xroot != yroot:  # which means they are not connected
            if self.rank[xroot] > self.rank[yroot]:
                self.parent[yroot] = xroot
            elif self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            else:
                self.parent[yroot] = xroot
                self.rank[xroot] += 1
    

    def connected(self, x, y) -> bool:
        return self.find(self.parent[self.mapping[x]]) == self.find(self.parent[self.mapping[y]])

    
numbers = [1, 4, 10, 5, 12, 56]
ur = UnionRank(numbers)
ur.union(1, 10)
print(ur.parent)
ur.union(4, 56)
print(ur.parent)
ur.union(4, 12)
print(ur.parent)
ur.union(1, 12)
print(ur.parent)
print(ur.connected(1, 56))