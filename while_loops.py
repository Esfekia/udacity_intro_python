card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of card_deck to the hand list
# until the values in hand add up to 17 or more

while sum(hand) < 17:
    hand.append(card_deck.pop())
    print(sum(hand))
print(hand)

#####################################
# Find the Factorial with While Loop:

# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current

    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)

##############################
# Find Factorial with For Loop:

# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
for i in range(1, number+1):
    product *= i
    i += 1

# print the factorial of number
print(product)
