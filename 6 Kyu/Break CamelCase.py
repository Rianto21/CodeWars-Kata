"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    upperword = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = ''
    for i in s:
        if i in upperword:
            string += ' {}'.format(i)
        else:
            string += i
    return string
