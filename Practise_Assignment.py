String1=input("Enter first string: ")

String2=input("Enter second string: ")


if(len(String1)>=len(String2)):
    long_string=len(String1)
    short_string=len(String2)
else:
    long_string=len(String2)
    short_string=len(String1)
    

for i in range(0,long_string):
   for j in range(0,short_string):
        if (String1[i]==String2[j]):
           
           continue
   print(String1[i])
           
           
abcd
cde