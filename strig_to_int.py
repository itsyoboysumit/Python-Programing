# Convert a string containing a number to an integer and perform arithmetic with it.

#checking data type
a='5555'
print(a)
data_type= type(a)
print (data_type)

#converting to int
b=int(a)
print(b)

#checking weather get converted to int or not
data_type=type(b)
print(data_type)

#performing arithmetic operations 
print(b+5)
print(b-5)
print(b*2)
print(b/5)
print(b%10)