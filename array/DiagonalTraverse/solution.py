class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        traversing matrix diagonally
        
        https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
        up - up one row and right one column
        down - down one row and left one column
        """
        
        num_rows = len(mat)
        num_cols = len(mat[0])
        result = []
        going_up = True
        cur_row = cur_col = 0
        while len(result) != num_rows * num_cols:
            if going_up:
                
                while cur_row >= 0 and cur_col < num_cols:
                    result.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                
                if cur_col == num_cols:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                
                going_up = False
            else:
                while cur_col >= 0 and cur_row < num_rows:
                    result.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                
                if cur_row == num_rows:
                    cur_row -= 1
                    cur_col += 2
                else:
                    cur_col += 1
                
                going_up = True
        
        return result
                
        
        