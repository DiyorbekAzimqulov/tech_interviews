def dec_to_bin(n):
    res = ''
    while n != 0:
        rem = n % 2
        n = n // 2
        res = str(rem) + res
    return res


def find_bin(number):
    # Write your code here
    # function which converts decimal number to binary string
    # iterate over range of number and use dec_to_bin and save it in Queue
    q = []

    for i in range(1, number + 1):
        q.append(dec_to_bin(i))
    return q
