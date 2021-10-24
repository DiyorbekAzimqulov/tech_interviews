# T->O(n) S->O(n)
# def two_sum(array: list, target_sum: int):
#     """
#         Function takes an array of numbers which is distinct and one interger.
#         it traverses all elements in array, we need two element in array that their sum is equal the target sum.
#         we create hash tables like dictionary in python, if y is the result of subtracting current element from target_sum,
#         if y is inside of table then x + y is target sum, else we put x inside of table.
#     """
#     hash_table = {}
#     for x in array:
#         # x + y = target_sum
#         # x is current element
#         y = target_sum - x
#         if y in hash_table:
#             result = [x, y]
#             return result
#         else:
#             hash_table[x] = x
#     return []


# T->O(n^2), S->O(1)
# def two_sum(array: list, target_sum: int):
#     for i in range(len(array)):
#         for j in array[i+1:]:
#             if array[i] + j == target_sum:
#                 return [array[i], j]
#     return []


# T-> O(n*log(n)), S->O(1)
# def two_sum(array: list, target_sum: int):
#     left = 0
#     right = len(array) - 1
#     array.sort() # Tim sort algorithm. O(n*log(n))
#     while(left < right):
#         if array[left] + array[right] == target_sum:
#             return [array[left], array[right]]
#         elif array[left] + array[right] < target_sum:
#             left += 1
#         else:
#             right -= 1
#     return []

# for test
# array = [5, 2, -5, 65, 22, 7]
# target_sum = 7
# result = two_sum(array, target_sum)
# print(result)