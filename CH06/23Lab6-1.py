def calcBMI(weight, height):
    return weight/height**2

if __name__ == "__main__":
    print("This program will calculate your BMI")    

    weight = eval( input( "Please enter your weight in pounds: ") )
    height = eval( input("Please enter your height in inches: ") )

    print("Your BMI is {:.2f}".format(calcBMI(weight * 0.45359237 , height * .0254)) )
