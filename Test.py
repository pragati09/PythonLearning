#Program to find uncommon letters between two strings and to make a new string by concatenating the uncommon letters.

String1=input("Enter first string: ")

String2=input("Enter second string: ")

a=set(String1)
b=set(String2)

print(a)
print(b)

c={x for x in String1 if x not in String2}
print('The letters in String1 which are not present in String2 are :',c)
d={y for y in String2 if y not in String1}
print('The letters in String2 which are not present in String1 are :',d)

joinedList = [*c, *d]
print('The uncommon letters between two strings are:',joinedList)
e=''.join(joinedList)
print('Concatenated string made up of uncommon letters between String1 and String2 is:',e)