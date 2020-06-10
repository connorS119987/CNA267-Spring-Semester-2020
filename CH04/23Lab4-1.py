#----------------------------------------#
#     Connor Seemann Seat 23 Lab 4.1     #
#----------------------------------------#

# Program that will find the cost of your bagels in the morinng
print("This program will find the cost of your bagels in the morning!")

ammount = int(input("How many bagels are ordered: ") )
cost = ammount * 0.60 if (ammount > 6) else ammount * 0.80 

print("The cost of {bagels} is ${cost:.2f}".format(bagels=ammount, cost=cost) )
