def two_sum(array: list, target_sum: int):
    hash_table = {}
    for x in array:
        y = target_sum - x
        if y in hash_table:
            result = [x, y]
            return result
        else:
            hash_table[x] = x
    return []

array = [1, 2, 3, 5, 8, 6]
target_sum = 14
result = two_sum(array, target_sum)
print(result)