# Leap Year
# More Simple way
def Is_leap_year(Year):
    if (Year % 400 == 0) or (Year % 4 == 0 and Year % 100 != 0):
        return True
    return False


# Here is the part where we are going to display also the months of Feb whether it is 29 days or 28 days
def days_in_month(Year, Month):
    Month_days = [31, 28, 31, 30, 31, 31, 30, 30]
    if Is_leap_year(Year) and Month == 2:
        return 29
    return Month_days[Month - 1]


# Here Is the output Data.
Year = int(input("Enter a year:  "))
Month = int(input("Enter a Month: "))
days = days_in_month(Year, Month)
print(days)
