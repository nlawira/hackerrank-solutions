# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

month, day, year = map(int, str(input()).split(" "))
dotw = calendar.weekday(year, month, day)
print(list(calendar.day_name)[dotw].upper())