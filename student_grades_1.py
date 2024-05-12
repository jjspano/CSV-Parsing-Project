import csv

with open('student_grades_1.csv', 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    print(header[0])
