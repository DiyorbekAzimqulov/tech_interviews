class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        traversing matrix diagonally
        
        https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
        up - up one row and right one column
        down - down one row and left one column
        our algorithm runs untill we store all elements in the matrix diagonally to the result array.

Going up 

for going up we first go one row up and one column to the right

while our current row is greater than or equal to 0 and we are not out of columns
it means we are in the grid
we append mat[row][col] to the result array
and decrement row by one for going up 
and increment column by one for going right
if column is out of grid it means we need to go back one column and down 2 row
we add 2 to our row to go down
and we decrement our column by one for coming to grid
if our row is less than 0 that means we are outside of grid by row 
so we need to add 1 to our row to go back to grid

Going down

For going down we first go down by one row and one column to the right 

while our current column is greater than or equal to 0 and we are not out of rows
it means we are in the grid
we append mat[row][col] to the result array
and decrement column by one for going left 
and increment row by one for going up
if row is out of grid it means we need to go up one row and  2 column to the right
we add 2 to our column to go right
and we decrement our row by one for coming to grid (going up)
if our column is less than 0 that means we are outside of grid by column
so we need to add 1 to our column to go back to grid



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
                
        
        