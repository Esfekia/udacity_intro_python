from pyparsing import Or


sentence = ["the", "quick", "brown", "fox",
            "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)


# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for number in range(5, 31, 5):
    print(number)


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []


# Write a for loop that iterates over the names
# list to create a usernames list.
# To create a username for each name, make everything
# lowercase and replace spaces with underscores.

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append((name.replace(" ", "_")).lower())

print(usernames)

# If we wanted to change the original list items itself:

usernames = ["Joey Tribbiani", "Monica Geller",
             "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].replace(' ', '_').lower()

print(usernames)

"""Tag Counter
Write a for loop that iterates over a list of strings, 
tokens, and counts how many of them are XML tags. 
XML is a data language similar to HTML. You can tell if a string 
is an XML tag if it begins with a left angle bracket "<" and 
ends with a right angle bracket ">". Keep track of the number 
of tags using the variable count."""

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in tokens:
    if i.startswith("<") and i.endswith(">"):
        count += 1

print(count)

# OR
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

"""Quiz: Create an HTML List
Write some code, including a for loop, that iterates over a list 
of strings and creates a single string, html_str, which is an HTML 
list."""


items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str = html_str+"<li>"+item+"</li>+\n"
html_str = html_str+"</ul>"

print(html_str)

# OR

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)
