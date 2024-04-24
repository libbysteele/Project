from datetime import datetime, timedelta
import calendar
# Prints a user friendly message
print("Please enter the month and year of a calendar you wish to see")
# Calculate Easter Sunday
def calculate_easter(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1

    return (month, day, year)
#Calculate Mother's day
def calculate_mothers_day(year):
    easter_month, easter_day, _ = calculate_easter(year)
    # Mother's Day is the fourth Sunday of Lent which is three weeks before Easter Sunday
    mothers_day_date = datetime(year, easter_month, easter_day) - timedelta(weeks=3)
    return (mothers_day_date.month, mothers_day_date.day)
#Calculate Good Friday
def calculate_good_friday(year):
    easter_month, easter_day, _ = calculate_easter(year)
    #Good Friday is two days earlier than Easter Sunday
    good_friday_date = datetime(year, easter_month, easter_day) - timedelta(days=2)
    return (good_friday_date.month, good_friday_date.day)
#Calculate Easter Monday
def calculate_easter_monday(year):
    easter_month, easter_day, _ = calculate_easter(year)
    #Easter Monday is the day after Easter Sunday
    easter_monday_date = datetime(year, easter_month, easter_day) + timedelta(days=1)
    return (easter_monday_date.month, easter_monday_date.day)
#Calculate May Bank Holiday
def calculate_may_bank_holiday(year):
    #Find the first of May
    may_first = datetime(year, 5, 1)
    #Find the first Monday in May
    while may_first.weekday() != calendar.MONDAY:
        may_first += timedelta(days=1)
    return(5, may_first.day)
#Calculate Father's Day
def calculate_fathers_day(year):
    #Find the first of June
    june_first = datetime(year, 6, 1)
    #Find the third Sunday of June
    fathers_day_date = june_first + timedelta(weeks =2, days=6-june_first.weekday())
    return (6, fathers_day_date.day)
#Define Custom Calendar class
class CustomCalendar(calendar.TextCalendar):
    def __init__(self, year, month, custom_holidays):
        super().__init__()
        self.year = year
        self.month = month
        self.custom_holidays = custom_holidays

    def formatday(self, day, weekday, width):
        if day != 0:
            for holiday, dates in self.custom_holidays.items():
                for date in dates:
                    if date[0] == self.month and date[1] == day:
                        return f'{day:2}*'
            return f'{day:2}'
        return '  '

    def list_starred_dates(self):
        starred_dates = []
        for holiday, dates in self.custom_holidays.items():
            for date in dates:
                if date[0] == self.month:
                    starred_dates.append((date[1], holiday))
        return starred_dates
#User friendly messages for erros 
def get_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid", data_type.__name__)
#Add custom holidays
def add_custom_holiday(custom_holidays):
    holiday_name = input("Enter the name of the holiday: ")
    while True:
        month = get_input("Enter the month of the holiday (1-12): ", int)
        if 1 <= month <= 12:
            break
        else:
            print("Invalid input. Month should be between 1 and 12.")
    while True:
        day = get_input("Enter the day of the holiday: ", int)
        if 1 <= day <= 31:
            break
        else:
            print("Invalid input. Day should be between 1 and 31.")
    if holiday_name not in custom_holidays:
        custom_holidays[holiday_name] = [(month, day)]
    else:
        custom_holidays[holiday_name].append((month, day))
    
year = get_input("Enter the year: ", int)
while True:
    month = get_input("Enter the month (1-12): ", int)
    if 1<= month <= 12:
        break
    else:print("Invalid input. Month Should be between 1 and 12.")
#Calculate Mother's Day for the specified year
mothers_day_month, mothers_day_day = calculate_mothers_day(year)
#Calculate May bank holiday for the specified year
may_bank_month, may_bank_day = calculate_may_bank_holiday(year)
#Calculate Good Friday for the specified year
good_friday_month, good_friday_day = calculate_good_friday(year)
#Calculate Easter Monday for the specified year
easter_monday_month, easter_monday_day = calculate_easter_monday(year)
#Calculate Father's Day for the specified year
fathers_day_month, fathers_day_day = calculate_fathers_day(year)
# Define custom holidays with dynamic dates
custom_holidays = {
    "New Year's Day": [(1, 1)],
    "New Year's Eve": [(12, 31)],
    "St Patrick's Day": [(3, 17)],
    "Summer Solstice": [(6, 21)],
    "Halloween": [(10, 31)],
    "Bonfire Night": [(11, 5)],
    "Boxing Day": [(12, 26)],
    "Christmas Eve": [(12, 25)],
    "Valentines Day": [(2, 14)],
    "Independence Day": [(7, 4)],
    "Christmas": [(12, 25)],
    "Easter Sunday": [calculate_easter(year)],
    "Good Friday": [(good_friday_month, good_friday_day)],
    "Easter Monday": [(easter_monday_month, easter_monday_day)],
    "Mother's Day (UK)": [(mothers_day_month, mothers_day_day)],
    "May Bank Holiday": [(may_bank_month, may_bank_day)],
    "Father's Day (UK)": [(fathers_day_month, fathers_day_day)]
}
#
while True:
    add_holiday = input("Do you want to add a custom holiday ? (yes/no): ").lower()
    if add_holiday == "yes":
        add_custom_holiday(custom_holidays)
    elif add_holiday == "no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
cal = CustomCalendar(year, month, custom_holidays)
print(cal.formatmonth(year, month))
starred_dates = cal.list_starred_dates()
if starred_dates:
    print("Holidays in", calendar.month_name[month], year)
    for date, holiday in starred_dates:
        print(f"{calendar.month_name[month]} {date}-{holiday}")
else:
    print("\nNo custom holidays in", calendar.month_name[month], year)
while True:
        another_calendar = input("Do you want to see another calendar? (yes/no): ").lower()
        if another_calendar == "yes":
            year = get_input("Enter the year", int)
            month = get_input("Enter the month (1-12): ", int)
            cal = CustomCalendar(year, month, custom_holidays)
            print(cal.formatmonth(year, month))
            starred_dates = cal.list_starred_dates()
            if starred_dates:
                print("Holidays in", calendar.month_name[month], year)
                for date, holiday in starred_dates:
                    print(f"{calendar.month_name[month]} {date}-{holiday}")
            else:
                print("\nNo custom holidays in", calendar.month_name[month], year)
        elif another_calendar == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
