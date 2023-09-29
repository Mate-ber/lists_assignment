import datetime

def days_in_month(year, month):
    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_per_month[2] = 29
    return days_per_month[month]

def display_calendar(year):
    for month in range(1, 13):
        first_day = datetime.date(year, month, 1)
        print(first_day.strftime("%B %Y").center(20, '-'))
        day_names = "Mo Tu We Th Fr Sa Su "
        print(day_names)
        day_of_week = first_day.weekday()
       # print(day_of_week)
        num_days = days_in_month(year, month)
      #  print(num_days)
        count_column=0
        days_in_line = ""
        for i in range(1, num_days + 1):
         #   print(i)
            if i==1:
                for j in range(0,day_of_week):
                    days_in_line+="   "
                    count_column+=3
            if i==num_days and count_column<20:
                days_in_line += str(i)
                print(days_in_line)
                break
            if count_column>=20:
                print(days_in_line)
                days_in_line=""
                count_column = 0
            if i<10:
                days_in_line += " "

            days_in_line += str(i)
            days_in_line += " "
            count_column +=3
            #    print(" ".join(days[i:i+7]))

        print()

current_year = datetime.date.today().year
next_year = current_year + 1
print(f"Calendar for the next year ({next_year}):")
display_calendar(next_year)

desired_year =int( input("Enter your desired year here:"))
print(f"Calendar for the desired year ({desired_year})")
display_calendar(desired_year)