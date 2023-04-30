# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

def productSum(array, depth=1):
    # Write your code here.
    total = 0
    for elem in array:
        if isinstance(elem, list):
            total += productSum(elem, depth=depth+1)
        else:
            total += elem
    return total * depth
    


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))

















