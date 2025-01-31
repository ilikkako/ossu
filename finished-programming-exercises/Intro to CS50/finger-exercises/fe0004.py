# Simple iteration practice

odd_number = None

for n in range(10):
    new_number = int(input("Enter a number: "))

    if new_number % 2 != 0 and odd_number == None:
        odd_number = new_number
    elif new_number % 2 != 0 and new_number > odd_number:
        odd_number = new_number

if odd_number == None:
    print("No odd number was entered!")
else:
    print("Highest odd number was: ", odd_number)
