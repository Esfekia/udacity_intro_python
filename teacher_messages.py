names = input("Please enter names, separated by commas:")
assignments = input("Please enter number of assignments, separated by commas:")
grades = input("Please enter grades, separated by commas:")
names_list = names.split(",")
assignments_list = assignments.split(",")
grades_list = grades.split(",")
i = 0
while i < len(names_list):
    name = names_list[i]
    assignment = assignments_list[i]
    grade = grades_list[i]
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n".format(
        name, assignment, grade, int(grade)+int(assignment)*2)
    print(message)
    i = i+1


# OR

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
