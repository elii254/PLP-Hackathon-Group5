career = ['developer', 'teacher']

advice = ['good', 'excellent']

quiz = ['Do you love coding?', 'are you a public speaker?']

print("Answer with yes or no")

developerCount = 0
teacherCount = 0
count = 0
for q in quiz:
    print(q)
    answer = input("Enter your answer: \n")
    if answer == "yes" and career[count] == "developer":
        developerCount = developerCount + 1
    if answer == "yes" and career[count] == "teacher":
        teacherCount = teacherCount + 1
    count += 1
if teacherCount > developerCount:
    print(career[1])
    print(advice[1])

elif teacherCount < developerCount:
    print(career[0])
    print(advice[0])
else:
    print("No career is suitable for you")
