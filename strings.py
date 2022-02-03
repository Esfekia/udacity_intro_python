# The \ divider allows you to use ' as part of the string.
salesman = '"I think you\'re an encyclopedia salesman"'
print(salesman)

# Notice len always results in an integer!
print(len("ababa") / len("ab"))

# Exercise 1:
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + " accessed the site " + url + " at " + timestamp + ".")

# Exercise 2:
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

# name_length =  # todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
name_length = len(given_name+" "+middle_names+" "+family_name)
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
