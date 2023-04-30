def generateDocument(characters, document):
    # Write your code here.
    chars_count = {}
    for char in characters:
        if char not in chars_count:
            chars_count[char] = 1
        else:
            chars_count[char] += 1
    for char in document:
        if char in chars_count and chars_count[char] > 0:
            chars_count[char] -= 1
        else:
            return False
    return True

