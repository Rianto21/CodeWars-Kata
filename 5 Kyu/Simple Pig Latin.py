"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    word = text.split(" ")
    new_word = ""
    for i in word:
        if i not in ['!','@','#','?','/']:
            new_word += i[1:] + i[0] +'ay '
        else:
            new_word += i + " "
    return new_word[:len(new_word)-1]
