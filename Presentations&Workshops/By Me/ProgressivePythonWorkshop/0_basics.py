# Welcome to Python! This file is going to try to get you up and running with the basics. 

# You can either run this whole python file with `python 0_basics.py` in the command line,
# or you can run it line by line through a python terminal or VSCode (shift+enter or ctrl+enter) 


print('Hello World') # This is how you print. Like everything in python, the functions usually have simple names

# (C++ note): In python you don't need to declare the type of any variables
x = 2

# These are if conditions
if x == 3:
    print('It be 3')
elif x > 3:
    print('Big')
else:
    print('Smol')

# You will notice we don't use { } to create code sections. Everything is separated by how indented it is.


numbers = [3, 5, 2, 8] # This is a 'list', kind of like an array in other languages but more powerful

# We can loop through a list but just saying 'in'
for n in numbers:
    print(n * 10)


# Alternatively, we can loop through numbers in a range
for n in range(5):
    print(n)


# Lets get a little weirder: let's make a list of words and a function to use with them
words  = ['Money', 'Printer', 'Go', 'Brr']


def add_dollar(word):
    new_word = '$' + word + '$' # We an append strings with a plus sign
    return new_word


for w in words:
    print(add_dollar(w))


# Final skill is importing packages. These provide super helpful tools that we are going to need.

# Numeric python
import numpy as np # Imports package and renames it 'np'

print(np.random.random())

# A note for matlab and R users: Python is objected oriented which means that we use a . to access functions that are wrapped inside other "objects". A package is an example of an object.