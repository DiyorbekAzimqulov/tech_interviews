from collections import deque  # double-ended queue
"""
https://leetcode.com/problems/find-if-path-exists-in-graph/description/
"""


class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int,
                  destination: int) -> bool:
        """
        form a graph from connections
            hash table to form a graph
        apply BFS
            keep track of visited nodes since it is bidectional

            [[0,1],[1,2],[2,0]]
            2, 0
            {0:[1], 1: [0, 2], 2:[0]}


        """
        # form a graph using hash tables
        graph = {}
        for edge in edges:
            s, d = edge
            if s not in graph:
                graph[s] = []
            if d not in graph:
                graph[d] = []
            graph[s].append(d)
            graph[d].append(s)
        # print(graph)
        if not graph and source == destination == 0:
            return True
        visited = []
        queue = deque()
        queue.extend(graph[source])
        while len(queue) > 0:
            node = queue.popleft()
            if node not in visited:
                if node == destination:
                    return True
                else:
                    visited.append(node)
                    queue.extend(graph[node])
        return False
