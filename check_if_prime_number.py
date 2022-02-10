# Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 67, 71, 73, 79, 85]
is_prime = False
# write your code here
for number in check_prime:
    for i in range(number-2):
        if number % (i+2) == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        print("{} is a prime number.".format(number))
    else:
        print("{} is NOT a prime number, because {} is a factor of {}".format(
            number, i+2, number))

# HINT: You can use the modulo operator to find a factor"""
