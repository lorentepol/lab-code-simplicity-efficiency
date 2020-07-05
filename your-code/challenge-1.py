"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

# let's create a lists with all possible outcomes and inputs, in string.

outcomes_str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                'negative five', 'negative four', 'negative three', 'negative two', 'negative one']
inputs_str = outcomes_str[0:6]

# now there is the calculus, the code is programmed in a way each number in 'string' has as its index within the list its
# numeric counterpart, such as inputs_str[5] = 'five' or outputs_str[-3] = 'negative three'
if (a in inputs_str) & (c in inputs_str):
    if b == 'plus':
        print('{} {} {} equals {}'.format(a,b,c, outcomes_str[inputs_str.index(a) + inputs_str.index(c)] ))
    elif b == 'minus':
        print('{} {} {} equals {}'.format(a,b,c, outcomes_str[inputs_str.index(a) - inputs_str.index(c)] ))
    else:
        print("I am not able to answer this question. Check your input.")
else:
    print("I am not able to answer this question. Check your input.")

print("Thanks for using this calculator, goodbye :)")