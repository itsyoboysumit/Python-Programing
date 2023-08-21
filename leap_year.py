'''Build a program to determine whether a given year is a leap year or not. If the year is divisible
 by 4 but not divisible by 100 (unless divisible by 400), it's a leap year.'''
year=int(input('Enter year:'))
if year%4==0 and year%100!=0 or year%400==0:
    print('Leap year')
else:
    print('Not a leap year.')