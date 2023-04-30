from typing import List


class Solution:

    def nearestValidPoint(self, x: int, y: int,
                          points: List[List[int]]) -> int:
        """
        a function or checker that checks whether a point is a valid point according to rule.
        all following operations are performed for valid points!
        store smallest distance and index in a hash table
        return smallest index with the distance
        [[1,2],[3,1],[2,4],[2,3],[4,4]]
        3, 4
        """
        cur_min = float('inf')
        cur_min_idx = -1
        for idx, point in enumerate(points):
            # check validness of a point to our current location
            x1, y1 = point
            if x == x1 or y == y1:
                distance = abs(x - x1) + abs(y - y1)
                if distance < cur_min:
                    # print(distance)
                    cur_min = distance
                    cur_min_idx = idx
        return cur_min_idx


x, y = 3, 4
points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
s = Solution()
print(s.nearestValidPoint(x=x, y=y, points=points))