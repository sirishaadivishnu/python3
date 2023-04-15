# Gradebook program to organize your subjects and grades
# Author: Sirisha Adivishnu
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]


subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Outermost "container" list
subjects_grades_gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]


subjects_grades_gradebook.append("computer science")
subjects_grades_gradebook.append(100)
subjects_grades_gradebook.append(["visual arts", 93])

subjects_grades_gradebook[-1][1] = 98

subjects_grades_gradebook[2].remove(85)
subjects_grades_gradebook[2].append('Pass')

full_gradebook = last_semester_gradebook + subjects_grades_gradebook

print(full_gradebook)







