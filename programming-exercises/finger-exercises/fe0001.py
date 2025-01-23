# Gather 3 numbers
x = input('Write integer: ')
y = input('Write integer: ')
z = input('Write integer: ')

# Input types are strings so we need to cast them to integers
x = int(x)
y = int(y)
z = int(z)

# If all of them are even, print smallest number
# If there is odd numbers, print the biggest odd number
answer = min(x, y, z)
if x % 2 != 0:
    answer = x
elif y % 2 != 0 and y > answer:
    answer = y
elif z % 2 != 0 and z > answer:
    answer = z
    
print(answer)
    