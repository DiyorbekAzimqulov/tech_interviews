# T->O(n) iterating over size n of an array, S->O(1) not using any extra space 
# def isValidSubsequence(array, sequence):
# # Write your code here.
#     array_index = 0
#     sequence_index = 0

#     while array_index < len(array):
#         if sequence_index == len(sequence):
#             break
#         if array[array_index] == sequence[sequence_index]:
#             array_index += 1
#             sequence_index += 1
#         else:
#             array_index += 1
#     if sequence_index == len(sequence):
#         return True
#     return False



array = [1, 1, 1, 1, 6, 1, 1]
subcequence = [1, 1, 1, 6, 1]
result = isValidSubsequence(array, subcequence)
print(result)