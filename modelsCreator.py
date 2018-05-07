"""

this file is used to create temp testing files for flow/ws matrix and so on

"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import numpy as np

csv_step_matrix_link = 'modelsStorage/tool_step_matrix/101_ingre_adder.csv'


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


def create_a_flow(flow_name):
    return flow_name


def create_a_equip_list(mainKind):
    # tool_main_kind = ['adder', 'baker', 'former', 'packager']
    tool_main_kind = [mainKind]
    # each kind is an area in some sense
    tool_adjectives = ['crazy', 'strong', 'mild', 'tiny']
    columns = ['ITEM_NO', 'WS', 'LOCATION', 'STATUS', 'PO_INFO',
               'IN_DATES', 'RLS_DATES', 'TIQ', 'CHAMBER_COUNT', 'OUT_DATES']
    number_of_equipment_per_ws = 4
    len_of_df = len(tool_main_kind)*len(tool_adjectives)*number_of_equipment_per_ws
    item_no_list = list(np.random.randint(10000, size=len_of_df))
    ws_names = [adj + '_' + kind for adj in tool_adjectives for kind in tool_main_kind]
    ws_list = [item for item in ws_names for i in range(number_of_equipment_per_ws)]
    location_list = 'loc_x'
    status_list = ['not sure']*len_of_df
    po_info_list = ['not sure']*len_of_df
    in_dates_list = ['11/3/2018', '3/1/2019', '5/1/2019', '3/3/2020'] * len(tool_main_kind)*len(tool_adjectives)


    equip_list_df = pd.DataFrame(columns=columns)
    equip_list_df.ITEM_NO = item_no_list
    equip_list_df.WS = ws_list
    equip_list_df.LOCATION = location_list
    equip_list_df.STATUS = status_list
    equip_list_df.PO_INFO = po_info_list
    equip_list_df.IN_DATES = in_dates_list
    # equip_list_df.RLS_DATES =
    equip_list_df.CHAMBER_COUNT = 3
    equip_list_df.set_index(keys='ITEM_NO', inplace=True)
    equip_list_df.TIQ = 60

    return equip_list_df

def create_a_WS(adj, kind):
    columns = ['KEY', 'STEP_NAME', 'FLOW', 'RPT', 'LS', 'UTIL',
               'CT', 'LOAD_PCT', 'LOAD_PREF', 'SUB_FLOW']

    # tool_main_kind = ['adder', 'baker', 'former', 'packager']
    # tool_main_kind = [mainKind]
    # each kind is an area in some sense
    # tool_adjectives = ['crazy', 'strong', 'mild', 'tiny']

    ws_name = adj + '_' + kind
    """
    biscuits of fate,bubur hitam,cake of destiny,pasta of tears
    
    """
    flow_list = 'biscuits_of_fate,bubur_hitam,cake_of_destiny,pasta_of_tear'.split(',')
    all_things_to_do = ['butter', 'salt', 'sugar', 'sage', 'sausage']
    verb = kind[:-2]

    newdf = pd.DataFrame(columns=columns)

    for a_flow in flow_list:
        selection = list(np.unique(np.random.randint(0,len(all_things_to_do),3)))
        things_to_do = [all_things_to_do[x] for x in selection]
        step_list = [adj + '_' + verb + '_' + x for x in things_to_do]
        lenDf = len(step_list)
        to_append_df = pd.DataFrame(columns=columns)
        # ['KEY', 'STEP_NAME', 'FLOW', 'RPT', 'LS', 'UTIL',
        #                'CT', 'LOAD_PCT', 'LOAD_PREF', 'SUB_FLOW']
        to_append_df.STEP_NAME = step_list
        to_append_df.FLOW = a_flow
        to_append_df.RPT = np.random.randint(1, 10, 1)[0]
        to_append_df.LS = 1
        to_append_df.UTIL = 0.65
        to_append_df.CT = 3
        to_append_df.LOAD_PCT = 1
        to_append_df.SUB_FLOW = 'FF,BACKEND'
        to_append_df.KEY = to_append_df.STEP_NAME + ' of ' + to_append_df.FLOW
        # to_append_df.set_index(keys='KEY', inplace=True)

        newdf = newdf.append(to_append_df.copy())

    newdf.set_index(keys='KEY', inplace=True)

    return newdf

def create_ws_time_info_of_a_mainkind(mainKind, adj_list):

    columns = ['WS', 'MA', 'UTIL', 'COMMENTS']
    newdf = pd.DataFrame(columns=columns)
    newdf.WS = [x + '_' + mainKind for x in adj_list]
    newdf.MA = 0.98
    newdf.UTIL = 0.75


    return newdf




# create_outs_target('2018-5-12', 60, 7).to_csv('modelsStorage/loading.csv')
# ['adder', 'baker', 'former', 'packager']
# df = create_a_equip_list('packager')
# df.to_csv('modelsStorage/aStudyName/tool_quan_matrix/packager.csv')
# print(df)
# main kind is like an area


# tool_main_kind = ['adder', 'baker', 'former', 'packager']
# tool_adjectives = ['crazy', 'strong', 'mild', 'tiny']

# tool_main_kind = [mainKind]
# each kind is an area in some sense
#

#for kind in tool_main_kind:
#    for adj in tool_adjectives:
#        folder_name = kind
#        file_name = adj + '_' + kind
#        tempDF = create_a_WS(adj, kind)
#        tempDF.to_csv('modelsStorage/aStudyName/tool_step_matrix/'
#                      + folder_name + '/'
#                      + file_name
#                      + '.csv')


tool_main_kind = ['adder', 'baker', 'former', 'packager']
tool_adjectives = ['crazy', 'strong', 'mild', 'tiny']

for kind in tool_main_kind:
    adf = create_ws_time_info_of_a_mainkind(kind, tool_adjectives)
    adf.set_index(keys='WS', inplace=True)
    adf.to_csv('modelsStorage/aStudyName/tool_time_matrix/' + kind + '.csv')


# output it..
print(adf)

