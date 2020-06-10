#------------------------------------#
#   Connor Seemann Seat 23 Lab 5.2   #
#------------------------------------#

# This program will tell people when they will be a millionaire from the amount they deposit with an intrest reate of 5.5%
print("This program will tell people when they will be a millionaire from the amount they deposit with an intrest reate of 5.5%\n\n")

a = 0       # a is the amount after t(1 + (r/n)) ** (nt) years
t = 0       # t is time in years
r = 0.055   # the rate is 5.5%
n = 1       # amount of times intrest is celcualted (

deposit = float( input("Enter your initial deposit: ") )
r       = float( input("Please enter the rate as a percentage (ex: 5.5): ") )
r       = r/100
n       = float( input("Please enter the amount of times compounding per year: ") )

while a <= 1000000:
    a = deposit*(1 + (r/n))**(n * t)
    t += .00001 # Making the output more exact number of years

print ("\nfrom an initial deposit of {} with a rate of {} and compounding {} time(s) per year,".format(deposit, r, n) )
print ("You will be a millionair in {:.4f} years!".format(t))
