# ORIGINAL SCRIPT:
# print("I am going to calculate your BMI.")
# height = float(input("How tall are you in meters?"))
# weight = float(input("How heavy are you in kilograms? "))
# print(f"Your BMI is {round((weight/(height)**2), 2}.")

# BONUS SCRIPT:
print("I am going to calculate your BMI.")
height_feet = float(input("How tall are you in feet? "))
height_inches = float(input("And how many inches? "))
weight_pounds = float(input("How heavy are you in pounds? "))
                          
height_meters = round((height_feet * 12 + height_inches) * 2.54 / 100, 2)
weight_kilos = round(weight_pounds * 0.453592, 2)
print(f"Your BMI is {round(weight_kilos / height_meters ** 2 , 2)}")
