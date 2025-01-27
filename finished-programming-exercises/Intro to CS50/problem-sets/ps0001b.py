# This program calculates the time in months you need to save for the down payment of your dream home
# while considering that you get semi-annual raises

yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save: ")) / 100
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a percent: ")) / 100 + 1
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
    if months % 6 == 0:
        yearly_salary *= semi_annual_raise

print('Number of months: ' + str(months))
