"""Quiz: Lambda with Map
map() is a higher-order built-in function that takes a function and iterable as inputs, 
and returns an iterator that applies the function to each element of the iterable. 
The code below uses map() to find the mean of each list in numbers to create the list averages. 
Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the mean function 
with a lambda expression defined within the call to map()."""
numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]

#mean = lambda num_list: sum(num_list) / len(num_list)


def mean(num_list): return sum(num_list) / len(num_list)

# def mean(num_list):
#    return sum(num_list) / len(num_list)


averages = list(map(mean, numbers))
print(averages)


"""Quiz 2: Lambda with Filter
The code below uses filter() to get the names in cities that are fewer than 10 characters long to create the list short_cities. 
Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter()."""

cities = ["New York City", "Los Angeles",
          "Chicago", "Mountain View", "Denver", "Boston"]

# def is_short(name):
#    return len(name) < 10


def is_short(name): return len(name) < 10


short_cities = list(filter(is_short, cities))
print(short_cities)
