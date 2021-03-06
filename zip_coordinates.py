"""Use zip to write a for loop that creates a string specifying the label 
and coordinates of each point and appends it to the list points. 
Each string should be formatted as label: x, y, z. For example, 
the string for the first coordinate should be 
F: 23, 677, 4."""
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for x, y, z, label in zip(x_coord, y_coord, z_coord, labels):
    points.append("{}: {}, {}, {}".format(label, x, y, z))

for point in points:
    print(point)

# Quiz: Zip Lists to a Dictionary
# Use zip to create a dictionary cast that uses names as keys and heights as values.

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
# replace with your code
print(cast)

# Quiz: Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72),
        ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)
