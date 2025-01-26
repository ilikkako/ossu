yearly_salary = int(input("What is your yearly salary: "))
portion_saved = int(input("How many percent of your salary you can save: ")) / 100
cost_of_dream_home = int(input("How much your dream home costs: "))
portion_down_payment = 0.25
full_down_payment = cost_of_dream_home * portion_down_payment
amount_saved = 0
return_rate = 0.05 
months = 0

# Calculate savings monthly 
while amount_saved < full_down_payment:
    amount_saved += amount_saved * (return_rate / 12)
    amount_saved += yearly_salary / 12 * portion_saved 
    months += 1 

print('Number of months: ' + str(months))
