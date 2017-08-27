# An example of a recursive function to
# find the factorial of a number

x = int(input("Enter a number: "))

def calc_factorial(x):

	if x==1:
		return 1
	else:
		return (x*calc_factorial(x-1))
		
print ("Factorial of",x,"is",calc_factorial(x))