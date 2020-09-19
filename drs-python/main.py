# This is a sample in Python for
# subject: Dates Range Check(DRS)
# created by: https://github.com/trolit

# Example
# Below code will validate if it's possible to rent house between given dates
# with "fake" collection. Real version with db connection can be extended to
# return for e.g. rents that dates are later than current one and only lasting ones.

import datetime


class Rent:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date


# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
class Color:
    OKBLUE = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# R1: 27.6.2020 - 15.7.2020
# R2: 23.7.2020 - 26.7.2020
# R3: 4.8.2020 - 19.8.2020
def get_booked_dates():
    var_rent1 = Rent(datetime.date(2020, 6, 27), datetime.date(2020, 7, 15))
    var_rent2 = Rent(datetime.date(2020, 7, 23), datetime.date(2020, 7, 26))
    var_rent3 = Rent(datetime.date(2020, 8, 4), datetime.date(2020, 8, 19))
    return [var_rent1, var_rent2, var_rent3]


def adjust_date_format(date):
    return date.strftime('%d.%m.%Y')


def validate_rent(rent):
    list_booked_dates = get_booked_dates()
    var_index = 0
    for booked_date in list_booked_dates:
        if rent.start_date < booked_date.end_date and rent.end_date > booked_date.start_date:
            return f'Rent between {adjust_date_format(rent.start_date)} and {adjust_date_format(rent.end_date)}' \
                   f' is not available' f' due to {adjust_date_format(booked_date.start_date)} - ' \
                   f'{adjust_date_format(booked_date.end_date)} reservation ' \
                   f'({Color.FAIL}R{(var_index + 1)}{Color.ENDC})'
        var_index += 1
    return f'Rent between {adjust_date_format(rent.start_date)} and {adjust_date_format(rent.end_date)} is available.'


# Attempts
print()
print(f'{Color.OKBLUE}A1:{Color.ENDC} {validate_rent(Rent(datetime.date(2020, 6, 20), datetime.date(2020, 6, 25)))} \n')
print(f'{Color.FAIL}A2:{Color.ENDC} {validate_rent(Rent(datetime.date(2020, 6, 26), datetime.date(2020, 6, 29)))} \n')
print(f'{Color.FAIL}A3:{Color.ENDC} {validate_rent(Rent(datetime.date(2020, 6, 29), datetime.date(2020, 7, 10)))} \n')
print(f'{Color.FAIL}A4:{Color.ENDC} {validate_rent(Rent(datetime.date(2020, 7, 20), datetime.date(2020, 7, 24)))} \n')
print(f'{Color.FAIL}A5:{Color.ENDC} {validate_rent(Rent(datetime.date(2020, 7, 20), datetime.date(2020, 7, 27)))} \n')
print(f'{Color.OKBLUE}A6:{Color.ENDC} {validate_rent(Rent(datetime.date(2020, 7, 27), datetime.date(2020, 8, 1)))} \n')
print(f'{Color.FAIL}A7:{Color.ENDC} {validate_rent(Rent(datetime.date(2020, 8, 15), datetime.date(2020, 8, 22)))} \n')
print(f'{Color.OKBLUE}A8:{Color.ENDC} {validate_rent(Rent(datetime.date(2020, 8, 20), datetime.date(2020, 9, 15)))}')
