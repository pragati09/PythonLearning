print("Enter the value of x: ")
x=int(input())

print("Enter the value of y: ")
y=int(input())

#Create an array of list with initial values filled with 0 or anything using the following code

z=[[0 for row in range(0,x)] for col in range(0,y)]
print(z)

#creates number of rows and columns for your array data.

#Read data from standard input:

for i in range(x):
         for j in range(y):
             z[i][j]=input()
#Display the Result:

for i in range(x):
         for j in range(y):
             print(z[i][j],end=' ')
         print("\n")