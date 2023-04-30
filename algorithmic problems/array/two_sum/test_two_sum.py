# O(n^2), O(1)
# def two_sum(array: list, target_sum: int):
#     for i in range(len(array)): # 0 -> n
#         for j in array[i+1:]: # n-1
#             if array[i] + j == target_sum:
#                 return [array[i], j]
#     return []


# O(n), O(n)
def two_sum(array: list, target_sum: int):
    table = {}
    for number in array:
        # number + result = target_sum
        result = target_sum - number
        if result in table:
            return [result, number]
        else:
            table[number] = number
    return []

array = [5, 3, 6, 8, -6, 1]
target_sum = 9
result = two_sum(array, target_sum)
print(result)