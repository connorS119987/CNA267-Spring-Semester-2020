def main(): # Defining the function of main
	try: #	try and except will catch all of the input errors or other errors in the program and will output the text accordingly
		
		#width = 4.5 #set width length
		width = eval( input("Width: ") ) # Makes user enter their own custom width | eval() evaluates the best type for the conversion rather than putting int() or float()
		
		#height = 7.9
		height = eval( input("Height: ") ) # Makes user enter their own custom hight | eval() evaluates the best type for the conversion rather than putting int() or float()

		perimeter = 2 * (width + height) # celculating the perimeter
		area = width*height # celculating the area
		
		print("The perimeter is", perimeter, "and the area is", area) # output
	
	except EOFError:
		print("EOFError occured, please try again..")
		print("Please make sure you enter a number")

		main() # wraps back to the start of the function

	except TypeError:
		print("TypeError occured...")
		print("Please make sure you enter numbers only!")

		main() # wraps back to the start of the function

	except: #catch all exception
		print("Other Error, something else went wrong...")
		
		main() # wraps back to the start of the function

if __name__ == "__main__": # When starting __name__ is == __main__ therefore this will only run once
	main() # goto main
