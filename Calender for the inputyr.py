import calendar
try:
  year=int(input("Enter the year(e.g,2025):")) #e.g is like an example for customer as to how to input


except ValueError: # means ki uper integer nahi input kuya to error
  print("invalid input, enter a valid numeric figure")
  exit()
  print(calendar.calendar(year))
