'''Implement a program that keeps asking the user to enter a password until they enter the correct one
 ("password123"). Print "Access granted" when the correct password is entered.'''

correctPassword="ppassword123"

while True:
    password = input('Enter your password:')
    
    if password == correctPassword:
        print('Acess Granted')
        break

    print('Incorrect Password')
