verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
verse_length = len(verse)
print ("\nVerse has a length of {}.".format(verse_length))

first_and = verse.find('and')
print ("\nIndex of first occurence of 'and' in Verse is {}.".format(first_and))

last_you = verse.rfind('you')
print ("\nIndex of last occurence of 'you' in Verse is {}.".format(last_you))

count_you = verse.count('you')
print ("\nCount of occurences of 'you' in Verse is {}".format(count_you))
