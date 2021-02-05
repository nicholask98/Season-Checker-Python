print('Welcome to my Season Checker')

input_month = input('Enter a month:\n').lower()
input_day = int(input('enter a day in that month just ints no suffix:\n'))

# Days since the beginning of the year at the start of the month
start_month_days = {
    'january': 0,
    'february': 31,
    'march': 59,
    'april': 90,
    'may': 120,
    'june': 151,
    'july': 181,
    'august': 212,
    'september': 243,
    'october': 273,
    'november': 304,
    'december': 334
    }
    
months_30_days = ['september', 'april', 'june', 'november']
    
# VALIDITY CHECKS -----
valid = True

# month validity check
if input_month not in start_month_days.keys():
    valid = False
# days validity check
if input_day > 31:
    valid = False
if input_month in months_30_days and input_day == 31:
    valid = False
if input_month == 'february' and input_day > 28:
    valid = False
if input_day < 1:
    valid = False
# --------

if valid == True:
    
    total_days = start_month_days[input_month] + input_day
    
    if 79 <= total_days <= 171:
        print('Spring')
    elif 172 <= total_days <= 264:
        print('Summer')
    elif 265 <= total_days <= 354:
        print('Autumn')
    else:
        print('Winter')
else:
    print('Invalid')