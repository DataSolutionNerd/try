# import random
import random as rd
import string
# List containing the names of my 5 favourite fruits
word_list = ['strawberry', 'kiwi', 'grapes', 'banana', 'orange']
# Print out the created list
print(word_list)


word = rd.choice(word_list)
print(word) 

print("Please enter a single letter input: ")
guess = input()
if len(guess) == 1 and guess.lower() in list(string.ascii_lowercase):
    print("Good guess")
else:
    print("Oops! That is not a valid input.")

