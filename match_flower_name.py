"""Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary.
The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name.
It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

Sample Output:

>>> Enter your First [space] Last name only: Bill Newman
>>> Unique flower name with the first letter: Bellflower"""

# Write your code here

# HINT: create a dictionary from flowers.txt
dict = {}
f = open("flowers.txt", 'r')
file_data = f.read()
print(type(file_data))

"""for line in file_data:
key, value = line.split()
dict[key] = value
print(dict)

# HINT: create a function to ask for user's first and last name


# print the desired output"""
