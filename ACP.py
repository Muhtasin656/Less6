import datetime
import calendar
current_date = datetime.datetime.now()
month_number = current_date.month
month_name = calendar.month_name[month_number]
print(f"Today's month is: {month_name}")