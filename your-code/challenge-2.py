"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    import random
    s = ''
    while len(s)<l:
        s += random.choice(a)
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        if a < b:
            import random
            c = random.choice(range(a, b+1))
        elif a == b:
            c = a
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

def input_integer(message):
    while True:
        try:
            x = int(input(message))
        except:
            print('Value not valid, please try again.')
            continue
        break
    return x
            
a = input_integer('Enter minimum string length: ')
b = input_integer('Enter maximum string length: ')
n = input_integer('How many random strings to generate? ')


print(BatchStringGenerator(n, a, b))