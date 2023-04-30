from collections import Counter

"""
Given two strings, write a method to decide if one is a permutation of the other.
"""

def is_permutation(string1: str, string2: str) -> bool:
    """
    # proposition 1
    using hash map, we store unique characters as keys and their occurances in string as values for the first string
    for second string to be permutation of the first one, characters and their occurances of the second string must equal to 
    the first string.
    so we iterate characters from the second string and if that character is present in the hashmap, we reduce its occurance
    if it is not present then it is not permutation
    time -> O(n)
    space -> O(m) where m is the number of unique characters.



    # proposition 2
    in order for two strings to be permutation to each other, their length must also be same.
    if two strings are sorted then they must be same

    time -> O(nlogn)
    space -> O(1)
    """
    # solution 1
    # counter = Counter(string1)
    # for char in string2:
    #     if char not in counter:
    #         return False
    #     if counter[char] == 1:
    #         del counter[char]
    #         continue
    #     counter[char] -= counter[char] - 1
    # return len(counter) == 0

    # solution 2
    # return sorted(string1) == sorted(string2)


str1 = "Cracking"
str2 = "rcaCking"
print(is_permutation(str1, str2))
