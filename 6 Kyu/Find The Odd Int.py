"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

def find_it(seq):
    just_one = set(seq)
    for x in just_one:
        if seq.count(x) % 2 == 1:
            return x
