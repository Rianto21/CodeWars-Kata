"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

def find_outlier(integers):
    even = list()
    odd = list()
    for x in range(len(integers)):
        if integers[x] % 2 == 0:
            even.append(integers[x])
        elif integers[x] % 2 == 1:
            odd.append(integers[x])
        if len(odd) == 1 and len(even) > 1:
            break
        elif len(even) == 1 and len(odd) > 1:
            break

    if len(even) == 1:
        return even[0]
    elif len(odd) == 1:
        return odd [0]
