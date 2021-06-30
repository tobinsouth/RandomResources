# In this files were going to analyse some text that we will download from a webpage.
# You need to find the answer to progress to the next challenge.
# We will write TODO when it is your turn to do work.

# Let discuss 4 facts

# 1: We can make text lowercase by applying a built in method of strings (.lower()) (The . means it is calling an object's function)
word = 'Tobin'
print(word.lower())

# 2: Looping through text
example_text = ['I', 'am', 'Sam', 'Sam', 'I', 'am']


# TODO: Print each word as a lower case using a for loop 



# 3: We can split longer text into a list of words
print('I am Sam Sam I am'.split())

# 4: We can test if a word is in a string using `in`
sam_text = 'I am Sam Sam I am'
if 'Sam' in sam_text:
    print('Indeed!')


if 'Tobin' in sam_text:
    print('Indeed!')
else:
    print('Go away Tobin!')



## Now comes the challenge

# First we import a package
import urllib.request 

# Second we load in the text from Green Eggs and Ham by Dr Seuss
greeneggs = "https://www.clear.rice.edu/comp200/resources/texts/Green%20Eggs%20and%20Ham.txt"
webpage = urllib.request.urlopen(greeneggs)
text = webpage.read().decode() # Don't worry about the details here, but ask if you're curious!


# TODO: Using the variable `text`, split it into words and count how many time Sam appears (using `in`) (might need to be lowercase?)












# TODO: The number of times Sam appears is the password to the next problem