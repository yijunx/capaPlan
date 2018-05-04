# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 18:57:37 2018

@author: xuyijun
it was mentioned as "bucket", long long time ago.
this is totally belong to a WS object
the purpose of separation, is because i want to keep I.O. function purely in WS
here is all the calculation stuff
"""

# from LoadingClass import Loading
#from WorkstationClass import Workstation


import pandas as pd
from date_time_operations import str_date_to_date_time
from date_time_operations import date_time_to_str_date
from date_time_operations import get_all_fridays
from date_time_operations import interval_plan_period
from date_time_operations import parse_a_matric
from datetime import date, timedelta
import matplotlib.pyplot as plt


class CapacityReport:
    def __init__(self, ws_util: 'general WS util', ws_step_matrix: 'the dataframe', assigned_moves: 'loading dataframe', equip_list: 'ws.equiplist'):
        self.is_report_latest = False
        # update to false if any, any assumption changed....
        self.comment = ''
        self.assigned_moves = assigned_moves
        self.util = ws_util
        self.equip_list = equip_list
        
        self.stepMatrix = ws_step_matrix
        self.report = pd.DataFrame()

    def run_assigned_moves(self, start_study_date: 'MM/DD/YYYY', end_study_date: 'MM/DD/YYYY'):
        """
        this method creates a bucket data frame
        :param start_study_date:
        :param end_study_date:
        :return:
        """
        self.is_report_latest = True
        step_flow_combos = list(self.stepMatrix.STEP_NAME + ' of ' + self.stepMatrix.FLOW)
        bucket_columns = []
        required_titles = ['MOVES', 'RPT', 'UTIL', 'LS', 'REQUIRED_TOOL']
        
        # well this is a lot of rows... but you can filter horizontally by
        # df.filter(like='MOVES', axis=1)
        # filter index col by
        # df.filter(like='22 CELL NIT', axis=1)

        for atitle in required_titles:
            bucket_columns = bucket_columns + [x + ': ' + atitle for x in step_flow_combos]
        # add the last two columns    
        bucket_columns = bucket_columns + ['TOTAL_TOOL_REQ','TOOL_AVAIL']
        # create a date time column in the outs target
        self.assigned_moves['DATETIME'] = self.assigned_moves.WEEK_START_DATE.apply(str_date_to_date_time)
        self.assigned_moves.set_index('DATETIME', inplace=True)
        self.report = pd.DataFrame(index = get_all_fridays(start_study_date, end_study_date),
                                      columns = bucket_columns)

        list_of_moves_date = list(self.report.index)
        
        # now lets fill in the moves for each WEEK
        # use df.at['scen_name', 'Value']
        for a_step_flow in step_flow_combos:
            list_of_CT = [parse_a_matric(self.stepMatrix.at[a_step_flow,'CT'],x) for x in list_of_moves_date]
            list_of_outs_dates = [x + timedelta(days=int(y * interval_plan_period()))
                                  for x, y in zip(list_of_moves_date, list_of_CT)]
            # easy move:  list_of_moves = [self.assigned_moves.at[a_step_flow, 'FLOW'] for x in list_of_moves_date]
            # not so easy move:
            list_of_moves = [sum([self.assigned_moves.at[x, self.stepMatrix.at[a_step_flow, 'FLOW'] + '.' + sub_flow]
                                  for sub_flow in self.stepMatrix.at[a_step_flow, 'SUB_FLOW'].split(',')])
                             for x in list_of_outs_dates]
            # list_of_moves = []
            # for a_move_date in list_of_outs_dates:
            # a_move = sum([self.assigned_moves.at[a_move_date, self.stepMatrix.at[a_step_flow, 'FLOW'] + subflow]
            # for subflow in ['.FF','.PCMOS']])
            #    list_of_moves.append(a_move)
            #    
            self.report[a_step_flow + ': MOVES'] = list_of_moves
            
            
            # [np.sum[self.assigned_moves.at[x,]
            # [self.stepMatrix.at[a_step_flow,'FLOW'] + '.' + subflow for subflow in self.stepMatrix.at[a_step_flow,'SUB_FLOW'].split())]    ]
            # for x in list_of_moves_date]
        
        # now lets fill in the  rpt
        for a_step_flow in step_flow_combos:
            list_of_RPT = [parse_a_matric(self.stepMatrix.at[a_step_flow,'RPT'],x) for x in list_of_moves_date]
            self.report[a_step_flow + ': RPT'] = list_of_RPT
            
        
        
        # now lets do util
        # for a_step_flow in step_flow_combos:
        #    list_of_RPT = [parse_a_matric(self.stepMatrix.at[a_step_flow,'RPT'],x) for x in list_of_moves_date]
        #    self.report[a_step_flow + ': RPT'] = list_of_moves
        for a_step_flow in step_flow_combos:
            self.report[a_step_flow + ': UTIL'] = self.util
        # now lets do ls
        for a_step_flow in step_flow_combos:
            list_of_LS = [parse_a_matric(self.stepMatrix.at[a_step_flow, 'LS'], x) for x in list_of_moves_date]
            self.report[a_step_flow + ': LS'] = list_of_LS
        
        # now lets get the required tool
        for a_step_flow in step_flow_combos:
            self.report[a_step_flow + ': REQUIRED_TOOL'] = (
                    self.report[a_step_flow + ': MOVES']
                    * self.report[a_step_flow + ': RPT']
                    / self.report[a_step_flow + ': LS']
                    / 10080
                    / self.report[a_step_flow + ': UTIL']
                    )
        
        # now lets get totoal required
        to_sum_list = [x + ': REQUIRED_TOOL' for x in step_flow_combos]
        self.report['TOTAL_TOOL_REQ'] = self.report[to_sum_list].sum(axis=1)
        
        # now lets get the tool avail from the equiplist...
        # need to total rls dates list
        rls_dates = []
        for index, row in self.equip_list.iterrows():
            if pd.isnull(row.KNOWN_RLS_DATES):
                to_append = row.CHAMBER_COUNT * [str_date_to_date_time(row.ODD) + timedelta(days = row.TIQ)]
                rls_dates = rls_dates + to_append
            else:
                to_append = [str_date_to_date_time(x) for x in row.KNOWN_RLS_DATES.split(',')]
                rls_dates = rls_dates + to_append
        
        print(rls_dates)
        
        self.report['TOOL_AVAIL'] = [sum([1 if x >= y else 0 for y in rls_dates]) for x in list(self.report.index)]
            
        return 0

    def print_to_excel(self):
        return 0
    
    def plot_chart(self):
        plt.scatter(self.report.index, self.report.TOTAL_TOOL_REQ)
        plt.show()

    def tool_req_when(self):
        return 0
    
    def tool_req_detail_when(self):
        return 0
    
    def tool_avail_when(self):
        return 0
    
    def tool_avail_detail_when(self):
        return 0

    
    
        

 
        
        
        





