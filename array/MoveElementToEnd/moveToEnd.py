# Complexity: T O(n), S O(n)
# def moveElementToEnd(array, toMove):
#     # Write your code here.
#     last_index = len(array) - 1
#     result = []
#     for number in array:
#         if number == toMove:
#             result.insert(len(result), number)
#         else:
#             result.insert(0, number)
#     return result
    
# Complexity: T O(n), S O(1)
# def moveElementToEnd(array, toMove):
#     # Write your code here.
#     left = 0
#     right = len(array) - 1
#     while (left < right):
#         while(array[left] != toMove and left < len(array) - 1):
#             left += 1
        
#         while(array[right] == toMove and right >= 0):
#             right -= 1
#         if right <= left:
#             break
#         tmp = array[left]
#         array[left] = array[right]
#         array[right] = tmp
#     return array

# array = [1, 2, 4, 5, 6]
# moveTo = 3
# result = moveElementToEnd(array, moveTo)
# print(result)