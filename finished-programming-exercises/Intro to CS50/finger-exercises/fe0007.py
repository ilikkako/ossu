"""Assume you are given a string variable named my_str. Write a piece of Python code that prints 
out a new string containing the even indexed characters of my_str. For example, if my_str = "abcdefg"
then your code should print out aceg."""

my_str = input("Enter a string: ")
new_str = ""

for c in my_str:
    c_index = my_str.index(c)
    if c_index % 2 == 0:
        new_str += c

print(new_str)