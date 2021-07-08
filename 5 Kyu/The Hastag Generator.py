"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""

def generate_hashtag(s):
    output = "#" #this was a base output only when 1<=len(s)<=140
    if len(s) == 0: return False #if nothing in s return False
    elif len(s) > 140: return False #if s string too long return False
    else:  #other than requirement in above
        for i in s.split(): #looping every elements in list of s.split()
            output += i.capitalize()  #and adding the capitalize one in to output 
    return output #return output after the loop
