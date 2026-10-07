# Question 3: This creates a usability issue because the system asks a user for an input when the user does not know what the system is asking for.
# Question 4: int() and float() convert the input into a integer or decimal, respectively. These are important when doing calculations on python because python can only calculate using numbers, and by not converting into a number you are trying to calculate using strings (impossible).

print("Enter the following information about an item you wish to purchase..")
print()

name = input("The name of the item: ")
# 2 differences between name and price input:
# Difference 1: The input of the name of the item was done on a seperate line rather than on the same line
# Difference 2: The second input needed to have the price converted to a float (decimal) but the first one didn't need to because it was a string.
price = float(input("The price: $"))

quantity = int(input("How many do you want? ")))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")
