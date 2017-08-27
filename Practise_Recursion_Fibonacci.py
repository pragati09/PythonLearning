# Python program to display the Fibonacci sequence up to n-th term using recursive functions

num = int(input("Enter a number: "))

def display_fibonacci(n):
	if n<=1:
		return n
	else:
		return (display_fibonacci(n-1)+display_fibonacci(n-2))
		
		
if num<=0:
	print("Please enter a positive integer")
else:
	print("Fibonacci series: ")
	for i in range(num):
		print(display_fibonacci(i))
		
