start_num = 1  # provide some start number
end_num = 1000  # provide some end number that you stop when you hit
count_by = 5  # provide some number to count by

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

######################
start_num = 15  # provide some start number
end_num = 1000  # provide some end number that you stop when you hit
count_by = 5  # provide some number to count by


# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = start_num
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value.Please try again."
else:
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)

################
limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)
