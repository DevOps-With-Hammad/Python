# 004 [Interactive Coding Exercise] Days in Month
def is_leap_year(Year):
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Here is the part where we are going to display also the months of Feb whether it is 29 days or 28 days
def days_in_month(Year, Month):
    Month_days = [31, 28, 31, 30, 31, 31, 30, 30]
    if is_leap_year(Year) and Month == 2:
        return 29
    return Month_days[Month - 1]


# Here Is the output Data.
Year = int(input("Enter a year:  "))
Month = int(input("Enter a Month: "))
days = days_in_month(Year, Month)
print(days)
