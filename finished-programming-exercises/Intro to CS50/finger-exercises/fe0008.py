# Finger Exercise Lecture 6
# Assume you are given an integer 0 \<= N \\<= 1000. Write a piece of Python code that uses bisection search to guess N. 
# The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N. 
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

n = int(input('Enter an integer please: '))
low = 0
high = 1000
guess = (low + high) / 2
count = 0

while guess != n:
    if guess > n:
        high = guess
    else:
        low = guess
    
    guess = round((low + high) / 2)
    count += 1

    print('guess: ', guess, 'count: ', count)

print('Count:', count)
print('Answer:', guess)
