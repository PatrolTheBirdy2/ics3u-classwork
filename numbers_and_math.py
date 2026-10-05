print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
# The f string evaluates 33 - 11 and places the resulting integer 22 directly into the text.
print(f"there are {33 - 11} boys.")
print()
# The f string evaluates the division 11 / 33 and uses round() to round the proportion of girls to 2 decimal places.
print(f"That means {round(11 / 33, 2)} % are girls...")
# The f string evaluates (33 - 11) / 33 and uses round() to round the proportion of boys to 2 decimal places.
print(f"and {round((33 - 11) / 33, 2)} % are boys.")
print()
print("If we made groups of six...")
# Floor division // divides 33 by 6 and takes the whole number portion of the answer, which is 5.
print(f"There would be {33 // 6} groups of six.")
# The modulus operator % finds the remainder when 33 is divided by 6.
print(f"And then a smaller group of {33 % 6} people.")
# This prints 30 "-" characters in a row.
print("-" * 30)
print("If we had 17 apples and 3 people...")
# Floor division 17 // 3 calculates the whole number of apples each person gets, which is 5.
print(f"Each person would get {17 // 3} whole apples.")
# The modulus operator 17 % 3 finds the remaining apples which is 2.
print(f"There would be {17 % 3} apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
# The f string evaluates 2 * 5 directly inside the curly braces to calculate the total cost $10.
print(f"they would each pay ${2 * 5}.")
