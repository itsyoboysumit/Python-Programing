'''
Write a program that checks if a given number is positive, negative, or zero. Print an appropriate
message based on the condition.
'''
a=int(input('Enter number:'))
if a<0:
    print('The given no is negative.')
elif a>0:
    print('The given no is positive.')
else:
    print('The given number is neither positive nor negative.')