points = 174  # use this input to make your submission

# write your if statement here
if points < 0 or points > 200:
    result = "Points cannot be negative, or above 200. Please try again."
elif points == 0:
    result = "Oh dear, no prize this time."
elif points >= 1 and points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points >= 51 and points <= 150:
    result = "Oh dear, no prize this time."
elif points >= 151 and points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
elif points >= 181 and points <= 200:
    result = "Congratulations! You won a penguin!"
print(result)

# Truth Value Testing Version:
points = 178  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit"
elif points <= 150:
    prize = None
elif points <= 180:
    prize = "wafer-thin mint"
elif points <= 200:
    prize = "penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time!"

print(result)


# '''
# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 8  # provide answer
guess = 8  # provide guess

if answer > guess:
    result = "Oops!  Your guess was too low."
elif answer < guess:
    result = "Oops!  Your guess was too high."
elif answer == guess:
    result = "Nice!  Your guess matched the answer!"

print(result)

state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state, total_cost)

print(result)
