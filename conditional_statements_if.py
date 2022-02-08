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
