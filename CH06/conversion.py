#This program will convert cups to fluid onces and vice versa

def cups_to_fluid(cups):
    return cups * 8
def fluid_to_cups(fluid):
    return fluid / 8

def main():
    print("This program will convert cups to fluid onces and vice versa")    

    function = input("Enter 1 for cups to fluid onces, enter 2 for fluid onces to cups: ") # Get input from user for what function they want
    
    if function == '1':
        cups = eval( input("Please enter the cups: ") ) # gets the amount of cups to convert
        print("There are {:.2f} fluid onces in {:.2f} cups".format(cups_to_fluid(cups), cups))
        function = input("Enter 1 for cups to fluid onces, enter 2 for fluid onces to cups: "); main()
    elif function == '2':
        fluid = eval( input("Please enter the fluid onces: ") ) # gets the amount of fluid onces to convert
        print("There are {:.2f} cups in {:.2f} fluid onces".format(fluid_to_cups(fluid), fluid))
        function = input("Enter 1 for cups to fluid onces, enter 2 for fluid onces to cups: "); main() 
    else:
        print("Please try again...") # Fall through protection
        main()

if __name__ == "__main__":
    main() # goes to main def
