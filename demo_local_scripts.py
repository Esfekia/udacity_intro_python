import useful_functions
scores = [88, 92, 79, 93, 85]

mean = useful_functions.mean(scores)
curved = useful_functions.add_five(scores)
mean_c = useful_functions.mean(curved)

print("Scores:", scores)
print("Original Mean: ", mean, " New Mean: ", mean_c)
