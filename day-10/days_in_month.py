def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True

    return False


def days_in_month(year, month):
    month_days = [31, (28 + int(is_leap(year))), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return month_days[month - 1]


year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)
