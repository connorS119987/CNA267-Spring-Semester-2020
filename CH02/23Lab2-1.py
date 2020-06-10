#Connor Seemann Seat 23 Lab 2.1

#Program that returns weekly pay
print("Program that will return amount you will be payed")

wage = eval( input("Enter the hourly wage: ") )
regHour = eval( input("Enter the number of regular hours: ") )
overHour = eval( input("Enther the number of overtime hours: ") )

totalPay = (wage * regHour) + (wage * (overHour * 1.5) )

print("The weekly pay you will recive is:", totalPay)
