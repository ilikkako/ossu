# Bisection search for square root

x = input("Enter an integer: ")
epsilon = 0.01
num_guesses = 0
low = 0
high = x
guess = (high + low) / 2
while abs(guess**2 - x) >= epsilon:
    if guess**2 > x:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2
    num_guesses += 1

print('number of guesses =', num_guesses)
print(guess, 'is close to square root of', x)
