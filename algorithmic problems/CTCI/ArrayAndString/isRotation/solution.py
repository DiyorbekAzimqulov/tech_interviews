
def is_substring(string: str, sub_string: str) -> bool:
    """
    given two strings, returns whether 2 string is the substring of the first one.
    """
    p1 = 0
    p2 = 0
    while p1 < len(string) and p2 < len(sub_string):
        if string[p1] != sub_string[p2]:
            p2 = 0
            p1 += 1
            continue
        p1 += 1
        p2 += 1
    return p2 == len(sub_string)

def is_rotation(s1: str, s2: str) -> bool:
    """
    returns whether s2 is the rotation of the s1

    s1 = bottleneck
                   ^
    s2 = ttleneckbo
                 ^
    conceptual overview
    so the rotation means their length are same. and characters also. but they rotated.
    so if string rotated then it divided into two parts. x and y. and xy is the whole string or yx. 
    if we find the parts x or y from the s2 then we use `is_substring` method to identify 
    other part is substring of the s1, if so then it is rotation.
    """
    p1 = 0
    p2 = 0
    while p1 < len(s1):
        if s1[p1] != s2[p2]:
            p2 = 0
            p1 += 1
            continue
        p1 += 1
        p2 += 1
    return is_substring(s1, s2[p2:])

s1 = "waterloo"
s2 = "loo water"

print(is_rotation(s1, s2))

