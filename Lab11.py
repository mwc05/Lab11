import os
import matplotlib.pyplot as plt
import math


fnames = os.listdir("data/submissions/")
students = {i[3:]: i[:3] for i in open("data/students.txt", "r").read().splitlines(False)}
assignments = [open("data/assignments.txt", "r").read().splitlines(False)[i:i + 3] for i in range(0, len(open(
    "data/assignments.txt", "r").read().splitlines(False)), 3)]
submissions = [open(f"data/submissions/{i}", "r").read().splitlines(False)[0].split("|") for i in fnames]
assignment_details = {}
for i in submissions:
    if i[1] in assignment_details:
        assignment_details[i[1]].append(int(i[2]))
    else:
        assignment_details[i[1]] = [int(i[2])]
print('''1. Student grade
2. Assignment statistics
3. Assignment graph
''')
selection = input("Enter your selection: ")
if selection == "1":
    name = input("What is the student's name: ")
    if name not in students:
        print("Student not found")
        exit()
    total_points = 0
    possible_points = 0
    for i in submissions:
        if i[0] == students[name]:
            for x in assignments:
                if x[1] == i[1]:
                    possible_points += int(x[2])
                    total_points += int(i[2])/100*int(x[2])
    print(f"{round(total_points/possible_points*100)}%")
elif selection == "2":
    assignment_name = input("What is the assignment name: ")
    if assignment_name not in [i[0] for i in assignments]:
        print("Assignment not found")
        exit()
    assignment_id = 0
    for i in assignments:
        if i[0] == assignment_name:
            assignment_id = i[1]
    print(f"Min: {math.floor(min(assignment_details[assignment_id]))}%")
    print(f"Avg: {math.floor(sum(assignment_details[assignment_id])/len(assignment_details[assignment_id]))}%")
    print(f"Max: {math.floor(max(assignment_details[assignment_id]))}%")
elif selection == "3":
    assignment_name = input('What is the assignment name: ')
    if assignment_name not in [i[0] for i in assignments]:
        print("Assignment not found")
        exit()
    assignment_id = 0
    for i in assignments:
        if i[0] == assignment_name:
            assignment_id = i[1]
    plt.hist(assignment_details[assignment_id], bins=[i for i in range(min(assignment_details[assignment_id]), max(assignment_details[assignment_id])+1, 5)])
    plt.show()
