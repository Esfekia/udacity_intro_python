"""Question: What type of loop should we use?
You need to write a loop that takes the numbers 
in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 
92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 
35, 173, 45, 149, 59, 84, 69, 113, 166]

Your code should add up the odd numbers in the list,
 but only up to the first 5 odd numbers together. 
 If there are more than 5 odd numbers, you should 
 stop at the fifth. If there are fewer than 5 odd 
 numbers, add all of the odd numbers."""
# Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_list = []
is_odd = 0
count = 0
list_sum = 0
while count < len(num_list) and is_odd < 5:
    if num_list[count] % 2 != 0:
        list_sum += num_list[count]
        odd_list.append(num_list[count])
        is_odd += 1
    count += 1

print(odd_list)
print("The sum of the odd numbers added is:{}".format(list_sum))
