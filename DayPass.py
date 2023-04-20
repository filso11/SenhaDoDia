#teste commit
import datetime
import pyperclip

today = datetime.datetime.now()

day = today.day
mounth = today.month
str_year = today.strftime("%y")
year = int(str_year)


def todayPass(day, mounth, year):
    return int(f"{day + year}{mounth + year}{year + year}")


pyperclip.copy(todayPass(day, mounth, year))
