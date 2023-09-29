import datetime


def days_in_month(year, month):
    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_per_month[2] = 29
    return days_per_month[month]

year=2024
line_str = ""
columns =4
month =1
to_hit = [0 for i in range(columns)]
start_month_nums = [0 for i in range(columns)]
stopped_at = [1 for i in range(columns)]
ch_month = month
for i in range(columns):
            first_day = datetime.date(year, ch_month, 1)
            num_days = days_in_month(year, ch_month)
            to_hit[i] = num_days
            start_month_nums[i] =  int( first_day.weekday() )
            ch_month += 1
ch_month = month
count_column =0
columns =4
for i in range(0,columns):
    count_column = 0
    for j in range(0, start_month_nums[i]):
        line_str += "   "
        count_column += 3
    print(f"i->{i} stopped->{stopped_at[i]} hit->{to_hit[i]} start onth->{start_month_nums[i]} count_column->{count_column}")
    for j in range(stopped_at[i], to_hit[i] + 1):
            if j < 10:
                line_str += " "
            line_str += str(j)
            line_str += " "
            if j == to_hit[i] and count_column <= 21:
                stopped_at[i] = j
                break
            if count_column >= 20:
                stopped_at[i] = j
                break
            stopped_at[i] = j
    line_str += "     "
  #  print(f"i->{i} stopped->{stopped_at[i]}")
print(line_str)