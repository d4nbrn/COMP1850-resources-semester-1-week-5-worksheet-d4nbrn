'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be achieved by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''

import csv 
filename = input("Please enter the name for your file")
dataList = []
i = 0


with open(filename,"r") as file:
     reader = csv.reader(file)
     for row in reader:
          dataList.append(row)

outfile = filename + "_out.csv"


for lists in dataList[1:]:
     student_id = lists[0]
     marks = 0
     subjectCount = 0
     del lists[0]
     for i in range(len(lists)):
          if lists[i] != "":
               marks = marks + int(lists[i])
               subjectCount += 1
     marks = marks/subjectCount
     if marks >= 70:
          grade = "1"
     elif marks >= 60:
          grade = "2:1"
     elif marks >= 50:
          grade = "2:2"
     elif marks >= 40:
          grade = "3" 
     else:
          grade = "F"
     outputList = [student_id,marks,grade]
     with open(outfile,"w") as outputFile:
          writer = csv.writer(outputFile)
          writer.writerow(outputList)