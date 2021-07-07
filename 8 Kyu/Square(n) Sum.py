"""
Translations
Collect|
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""

def square_sum(numbers):
    total = 0  #to calculate all power of 2 in the list
    for x in numbers:  #for every element in numbers
        total += x **2  #we add value of total by element of numbers power 2
    return total  #return the total
