vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
result=[x*2 for x in vec]
print(result)
# filter the list to exclude negative numbers
result1=[x for x in vec if x >= 0]
print(result1)
 # apply a function to all the elements
result2=[abs(x) for x in vec]
print(result2)
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
result3=[weapon.strip() for weapon in freshfruit] #strip() removes leading and trailing spaces
print(result3)
# create a list of 2-tuples like (number, square)
result4=[(x, x**2) for x in range(6)]
print(result4)
# flatten a list using a listcomp with two 'for'
vec1 = [[1,2,3], [4,5,6], [7,8,9]]
result5=[num for elem in vec1 for num in elem]
print(result5)