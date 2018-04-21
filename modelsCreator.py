"""

this file is used to create temp testing files for flow/ws matrix and so on

"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

csv_step_matrix_link = 'modelsStorage/stepMatrix.csv'


def products():
    """
    this function returns a number of products
    :return:
    """
    a_step_matrix = pd.read_csv(csv_step_matrix_link, index_col=0, header=0)
    # read the ws csv and create first...
    # print(np.ndarray.tolist(a_step_matrix['flow name'].unique()))

    return list(a_step_matrix['flow name'].unique())


def create_outs_target(start_date, number_of_intervals, interval_length):

    start_date = pd.to_datetime(start_date)
    print(start_date)
    print(start_date + timedelta(interval_length * number_of_intervals))
    days = pd.date_range(start_date, start_date + timedelta(interval_length * (number_of_intervals - 1)),
                         freq=str(interval_length) + 'D')
    outs_target = pd.DataFrame(data=np.random.randint(low=0, high=200, size=(number_of_intervals, len(products()))),
                               index=days,
                               columns=products())
    print(outs_target)

    return outs_target


create_outs_target('2018-5-12', 60, 7).to_csv('modelsStorage/outs_target.csv')
# output it..


