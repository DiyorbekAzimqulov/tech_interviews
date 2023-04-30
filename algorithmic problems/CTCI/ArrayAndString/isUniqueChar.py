"""
Implement an algorithm if a string has all unique characters. What if you can not use additional data structure?
"""

def is_unique(string: str) -> bool:
    """
    determines whether the given string contains unique characters
    """
    # solution 1 (hash set)  # time - O(n) | space - O(1) (all characters is a finite set)
    # uniques = set()
    # for char in string:
    #     if char in uniques:
    #         return False
    #     else:
    #         uniques.add(char)
    # return True

    # solution 2 (array) # time - O(n^2) | space - O(1)
    # string2 = ""
    # for char in string:  # O(n)
    #     if char in string2:  # O(n)
    #         return False
    #     else:
    #         string2 += char  # O(n)
    # return len(string) == len(string2)

    # solution 3 (bit vector)
    raise NotImplementedError("Solution has not yet provided")

string = "temur"
print(is_unique(string))