from datetime import date
today=date.today()
# splitDate=today.split("-")
year, month, day = int(today.year), int(today.month), int(today.day)
print(year, month, day)