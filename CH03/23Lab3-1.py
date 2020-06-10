#----------------------------------------#
#     Connor Seemann Seat 23 Lab 3.2     #
#----------------------------------------#

# Program that celculates BMI from user input
print("Celculates Body mass index from input")

# Getting user height and weight in imperial measurements
weightInPounds = eval( input("Please input your weight in pounds: ") )
heightInInches = eval( input("Please enter your height in inches: ") )

# Conversion from imperial to metric systems
weightInKilo = weightInPounds * 0.45359237  # 0.45359237 = 1 pound
heightInMeters = heightInInches * 0.0254    # 0.0254 = 1 inch

# BMI formula = Weight / Height^2
BMI = weightInKilo / (heightInMeters**2)

print( "Your BMI is {:.2f}".format(BMI) )
