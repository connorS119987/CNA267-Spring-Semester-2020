# Will determin the minimum length of runway an aircraft needs to take off

print("This program will determin the minimum length of runway an aircraft needs\n") # Prints introduction statement

v = eval( input("Please enter the take-off speed of the aircraft: ") )  # Obtaining the velocity of the aircraft
a = eval( input("Please enter the acceleration of the aircraft: ") )    # Obtaining the acceleration of the aircraft

""" Formula for length of runway needed is the following """
"""                 lenght = ( (v**2) / 2 ) * a          """

length = ( v**2 / (2 * a) )

print("The minimum runway length for this aircraft is", length, "meters.")
