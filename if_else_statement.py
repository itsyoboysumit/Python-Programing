''' Create a program that determines whether a person is eligible to vote. If the person'
s age is 18 or above, print "You are eligible to vote," otherwise print "You are not eligible to vote.'''
age=int(input('Enter your age:'))
if age<18:
    print('Your are not eligible to vote.')
else:
    print('Your are eligible to vote.')