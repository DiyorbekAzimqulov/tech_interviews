from stack import MyStack

expression = [
    "-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18",
    "8", "*", "-86", "-", "-", "16", "/", "26", "-14", "-", "-", "47", "-",
    "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*",
    "-60", "+", "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44",
    "*", "180", "70", "-40", "-", "*", "86", "132", "-84", "+", "*", "-", "38",
    "/", "/", "21", "28", "/", "+", "83", "/", "-31", "156", "-", "+", "28",
    "/", "95", "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73", "/",
    "-62", "/", "93", "*", "196", "-", "-59", "+", "187", "-", "143", "/",
    "-79", "-89", "+", "-"
]
stack = MyStack()
operators = ['-', '*', '+', '/']
for token in expression:
    if token not in operators:
        stack.push(int(token))
    else:
        f = stack.pop()
        s = stack.pop()
        if token == '-':
            result = s - f
            print(f'{result} = {s} - {f}')
        elif token == '+':
            result = s + f
            print(f'{result} = {s} + {f}')
        elif token == '/':
            result = int(s / f)
            # if result < 0:
            #     if abs(s) // abs(f) < 1:
            #         result = 0
            print(f'{result} = {s} // {f}')
        elif token == '*':
            result = s * f
            print(f'{result} = {s} * {f}')
        stack.push(result)
print(stack.stack_list)