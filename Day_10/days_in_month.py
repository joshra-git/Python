def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     it_is = is_leap(year)
#     if it_is == "Leap year.":
#         month_days[1] = 29
#         # print(is_leap(year))
#     month = month -1
#     month_num = month_days[month]
#     return month_num

# This is her code. Instead of returning "Is leap year" she's setting it to a boolean with True and False
# with line 30, if is_leap(year) would each True if it is and False if it isn't. so if "value" seems to output True or False 
# That's a bit confusing but it kind of makes sense. "if 1" is if true and if not 1 is false


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    month_num = month_days[month - 1]
    return month_num


#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)