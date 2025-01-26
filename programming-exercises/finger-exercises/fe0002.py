# This program checks if number is zero, negative or positive.

x = input("Write a number: ")
x = int(x)

if x < 0:
    print('The number is negative')
elif x == 0:
    print('The number is zero')
else:
    print('The number is positive')
