#----------------------------------#
#   Connor Seemann Seat 23 Lab 5   #
#----------------------------------#

#This program will calculate the average and the total of numbers entered
print("This program will calculate the average and the total of numbers entered\n")

num = 1
entered = []

while True: #making this loop true until the break

    num = float( input("Please enter any number, to quit enter 0:\n") ) # getting the user input
    
    if num == 0 and len(entered) != 0: # checking for the quit statement
        break
    
    elif num == 0 and len(entered) == 0: # catches if the user has only entered 0 and resets the list
        print("You didn't enter any numbers...\n please try again\n")
        entered = []
    
    elif num != 0: # Continues normally and appends num to the entered list
        entered.append(num)
    
    else: # catches fall throughs for variables I didn't account for
        print("Please make sure you entered an integer...")

total = 0

for i in entered: # this loop will add the numbers together
    total += i

# output statements
print("You entered {} numbers.".format(len(entered)) )
print("The total is", total)
print("The average is", total/len(entered) )
