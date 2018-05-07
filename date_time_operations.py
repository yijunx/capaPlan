# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 16:09:37 2018

@author: xuyijun
"""

from datetime import timedelta
from datetime import datetime

# adate = datetime.strptime('12/12/2018','%m/%d/%Y')
# print(adate.strftime('%B %d, %Y))

def interval_plan_period():
    return 7


def str_date_to_date_time(str_date: 'MM/DD/YYYY/'):
    return datetime.strptime(str_date, '%m/%d/%Y')


def date_time_to_str_date(datetime_obj):
    return datetime_obj.strftime('%m/%d/%Y')


def get_all_fridays(from_date: 'MM/DD/YYYY/', to_date: 'MM/DD/YYYY/', day_list=[5]):
    tmp_list = list()
    date_list = list()
    # Creates a list of all the dates falling between the from_date and to_date range
    for x in range((str_date_to_date_time(to_date) - str_date_to_date_time(from_date)).days + 1):
        tmp_list.append(str_date_to_date_time(from_date) + timedelta(days=x))
    for date_record in tmp_list:
        if date_record.weekday() in day_list:
            date_list.append(date_record)

    return date_list


def parse_a_matric(matric, moves_date):

    if ';' in str(matric):
        # use the whatever thats has been writeen
        the_matric_wanted_at_moves_date = matric

        # imagine the string is '09/03/2018,20;9/3/2019,10'
        # list_of_dates
        # list_of_values

    else:
        return matric

    return the_matric_wanted_at_moves_date


def write_a_matric():
    the_parse_able_string = 0
    return the_parse_able_string

def check_a_matric():
    return 0