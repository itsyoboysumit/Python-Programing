''' Write a program that prints all even numbers from 1 to 20, but skips the number 10 using the 
continue statement.'''

for i in range (1,21):
    if i==10:
        continue
    if i%2==0:
        print(i,end=' ')