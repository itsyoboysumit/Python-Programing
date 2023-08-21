''' Create a grading program that takes a student's score as input and prints the corresponding grade.
 Use elif statements to handle different ranges of scores.'''

marks= int(input('Enter your marks:'))
if marks<40 and marks>0:
    print('Fail')
elif marks>40 and marks<=50:
    print('Grade E')
elif marks>50 and marks<=60:
    print("Grade D")
elif marks>60 and marks<=70:
    print('Grade C')
elif marks>70 and marks<=80:
    print("Grade B")
elif marks>80 and marks<=90:
    print("Grade A")
elif marks>90 and marks<=100:
    print('Grade A++')
else:
    print('Invalid Marks')
