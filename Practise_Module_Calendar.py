#Python program to display calendar of given month of the year

#import module
import calendar

#Ask month and year from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))