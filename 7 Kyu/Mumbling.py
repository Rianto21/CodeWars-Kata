"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def accum(s):
    data = ''
    indeks = 1
    for i in s:
        if indeks < len(s):
            data += i.upper() + i.lower()*(indeks-1) + '-'
        elif indeks == len(s):
            data += i.upper() + i.lower()*(indeks-1)
        indeks += 1
    return data
