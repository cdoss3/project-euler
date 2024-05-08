"""

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

sunday_count = 0

class Month:

    def __init__(self, name, calendar_num, num_of_days):
        self.name = name
        self.calendar_num = calendar_num
        self.num_of_days = num_of_days

    def __repr__(self):
        return self.name


january = Month('January', 1, 31)
february = Month('February', 2, 28)
february_ly = Month('February leapt', 2, 29)
march = Month('March', 3, 31)
april = Month('April', 4, 30)
may = Month('May', 5, 31)
june = Month('June', 6, 30)
july = Month('July', 7, 31)
august = Month('August', 8, 31)
september = Month('September', 9, 30)
october = Month('October', 10, 31)
november = Month('November', 11, 30)
december = Month('December', 12, 31)


month_dict = {
    1: january,
    2: february,
    3: march,
    4: april,
    5: may,
    6: june,
    7: july,
    8: august,
    9: september,
    10: october,
    11: november,
    12: december,
}

# Initialize the date at Jan 1, 1900, and count the day

day = 1
month = 1
year = 1900
day_counter = 1

# Count to the year 2000

while year < 2001:
    # When the month counter resets past 12 reset to 1 (Jan)
    month = 1
    
    while month < 13:

        # When the day counter resets past the days in the month reset to the 1st of the next month
        day = 1

        # Check for leap years and february to reset after 29 days instead of 28
        if year % 4 == 0 and year != 1900 and month == 2:
            while day <= 29:

                # Only count the first Sundays
                if day_counter % 7 == 0 and day == 1:
                    sunday_count += 1
                    
                day += 1
                day_counter += 1
        
        # If it's not a leap year, proceed as normal
        else:
            while day <= month_dict[month].num_of_days:
                if year != 1900:

                    # Only count the first Sundays
                    if day_counter % 7 == 0 and day == 1:
                        sunday_count += 1
                day += 1
                day_counter += 1
        month += 1
    year += 1

print(sunday_count)