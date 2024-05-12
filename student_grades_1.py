import csv

with open('student_grades_1.csv', 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    for row in reader:
       student_first_name = row[0]
    student_last_name = row[1]
    student_year = row[2]
    student_grade = row[3]
    line = f"{student_first_name} {student_last_name} is in year {student_year} and got a grade of {student_grade}."
    print(line)    
