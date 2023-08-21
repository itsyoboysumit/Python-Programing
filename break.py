'''Create a program that prompts the user to enter a series of numbers. Keep accepting numbers until the 
user enters a negative number. Calculate and print the sum of the positive numbers.'''
sum=0
while True:
    num = int(input('Enter number:'))
    if(num<0):
        break
    sum= sum+num
print(sum)       