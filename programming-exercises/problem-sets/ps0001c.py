# Follow up for ps0001a & b. This program looks for lowest rate of return so that you can save down payment for a house in three years.
# To achieve these results it uses bisectional search

initial_deposit = float(input("Enter initial deposit: "))
cost_of_the_house = 800000
down_payment = cost_of_the_house * 0.25

months = 36
limit = 100
number_of_guesses = 0
low_boundary = 0
high_boundary = 1.0
r = (low_boundary + high_boundary) / 2
amount_saved = initial_deposit * (1 + r/12)**months


# Bisectional search, find the smallest rate of return, if not possible in 3 years return none
while abs(amount_saved - down_payment) >= limit :
    if amount_saved < down_payment:
        low_boundary = r
    else:
        high_boundary = r

    r = (low_boundary + high_boundary) / 2
    amount_saved = initial_deposit * (1 + r/12)**months

    if initial_deposit * (1 + 1/12)**months < down_payment:
        r = None
        break

    number_of_guesses += 1  
    

print("Best savings rate: ", r)
print("Steps in bisection search: ", number_of_guesses)
