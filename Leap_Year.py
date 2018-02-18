"""In the Gregorian calendar three criteria must be taken into account to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year."""

def is_leap(year):
    if (year%400==0):
        return True
    elif(year%100==0):
        return False
    elif(year%4==0):
        return True
    else:
        return False

year = int(input("Enter Year :: "))
print(is_leap(year))
