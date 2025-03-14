"""Write a program that asks the user to enter an integer and
prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
to the integer entered by the user. If no such pair of integers exists, it should
print a message to that effect."""

def find_root_pwr():
    num = int(input("Enter an integer: "))
    found = False
    
    for pwr in range(2, 6):  # pwr ranges from 1 to 5
        root = round(num ** (1 / pwr))  # Estimate root
        if root ** pwr == num:
            print(f"root: {root}, pwr: {pwr}")
            found = True
            break  # Stop at the first found pair
    
    if not found:
        print("No such pair of integers found.")

# Run the function
find_root_pwr()
