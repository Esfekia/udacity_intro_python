"""Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary.
The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name.
It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

Sample Output:

>>> Enter your First [space] Last name only: Bill Newman
>>> Unique flower name with the first letter: Bellflower"""

# Write your code here

# HINT: create a dictionary from flowers.txt


from venv import create


def create_flowerdict(myfile):
    myfile = open(myfile, 'r')
    data_dict = {}
    for line in myfile:
        key, value = line.strip().split(":")
        data_dict[key.strip()] = value.strip()
    myfile.close()
    return data_dict


# HINT: create a function to ask for user's first and last name
def main():
    flower_d = create_flowerdict("flowers.txt")
    first_name = input("Please enter your first name:")
    last_name = input("Please enter your last name:")
    # print the desired output"""
    print("Unique flower name with the first letter:" +
          flower_d[first_name[0]])


main()
