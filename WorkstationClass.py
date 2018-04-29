"""
this is the first PY file on online...
Git hub is so good


"""

import pandas as pd
import numpy as np
from LoadingClass import Loading


class Workstation:

    # def map_a_step(self, stepname, rpt, loadsize: 'use 1 for single wafer', util: 'put 0 if using WS util', inflow):
    #    self.stepMatrix.append()
    #    return 0
    def __init__(self, ws_link, ws_step_matrix_link, tool_count_link):
        """
        :param name:fff
        :param util:fff
        """
        self.name = os.path.split(ws_step_matrix_link)[1][:-4]
        self.ws_link = ws_link
        self.tool_count_link = tool_count_link
        self.ws_step_matrix_link = ws_step_matrix_link
        self.stepMatrix = pd.read_csv(self.ws_step_matrix_link, header = 0, index_col = 0)
        ma_util_table = pd.read_csv(self.ws_link, header = 0, index_col = 0)
        self.util = ma_util_table.loc[self.name, 'UTIL']
        self.ma = ma_util_table.loc[self.name, 'MA']
        tool_count_table = pd.read_csv(self.tool_count_link, header = 0, index_col = 0)
        self.equip_list = tool_count_table[tool_count_table.WS == self.name]
        
        #those about bucket
        #self.assigned_moves = pd.DataFrame()
        self.bucket = CapacityReport(self.util, self.stepMatrix,pd.DataFrame(),self.equip_list)
        
    
    def assign_moves(self, outs_target):
        # self.assigned_moves = outs_target
        self.bucket.assigned_moves = outs_target
        self.bucket.is_report_latest = False
        
        


    def update_a_step(self,
                      step_name,
                      in_flow: 'flow name pls',
                      what_to_change: 'put rpt/ls/util',
                      new_value: 'put a number'):
        """
        :param step_name:a
        :param in_flow:a
        :param what_to_change: a string
        :param new_value: a string of desc is also OK, please check the format
        :return: triggers email to send something
        """
        # check if the what_to_change is valid
        if not (what_to_change in ['rpt', 'ls', 'util']):
            print('this change is not valid')
            return -2

        # check if the step_name/in_flow combo is new or existing in the matrix
        if any(np.array((self.stepMatrix['step name'] == step_name) & (self.stepMatrix['flow name'] == in_flow))):
            target_index = self.stepMatrix.loc[
                (self.stepMatrix['step name'] == step_name) & (self.stepMatrix['flow name'] == in_flow)].index
            self.stepMatrix.at[target_index, what_to_change] = new_value

        else:
            print('this step/flow combo is not in current model, please add a step')
            # the step is not in there, hence this is a new step

        return 0

    def add_a_step(self, step_name, in_flow, rpt, ls, util):
        """

        :return:
        """
        if any(np.array((self.stepMatrix['step name'] == step_name) & (self.stepMatrix['flow name'] == in_flow))):
            # the step is already in here....
            print('this step is already here, cannot add, please modify')
            return -1

        new_step = pd.DataFrame(columns=list(self.stepMatrix.columns.values))
        new_step.loc[0] = [step_name, in_flow, rpt, ls, util]
        print(new_step)
        self.stepMatrix = self.stepMatrix.append(new_step, ignore_index=True)
        # then arrange
        self.arrange_steps()
        return 0

    def remove_a_step(self, step_name, in_flow):
        if any(np.array((self.stepMatrix['step name'] == step_name) & (self.stepMatrix['flow name'] == in_flow))):
            # it exits
            target_index = self.stepMatrix.loc[
                (self.stepMatrix['step name'] == step_name) & (self.stepMatrix['flow name'] == in_flow)].index
            self.stepMatrix.drop(index=target_index, inplace=True)
        else:
            print('the step / flow not there....nothing to remove')
            return 0

        # then arange
        self.arrange_steps()
        return 0

    def arrange_steps(self):
        """

        :return:
        """

        self.stepMatrix.sort_values(by=['step name', 'flow name'], inplace=True)
        self.stepMatrix.reset_index(drop=True, inplace=True)
        return 0

    def delete_column_in_matrix(self, column_name):
        """

        :param column_name:
        :return:
        """
        return 0

    def export_to_csv(self, csv_link):
        self.stepMatrix.to_csv(csv_link)
        return 0

    def map_steps_from_csv(self, csv_link):
        """

        :param csv_link:
        :return:
        """

        self.stepMatrix = pd.read_csv(csv_link, index_col=0, header=0)
        # need to check if there is duplicate combo and step/flow

        return 0

    def mass_update(self):
        """
        this one changes the step name in all flows
        this is a one shot file... not for any purpose

        """
        # w['female'] = w['female'].map({'female': 1, 'male': 0})
        self.stepMatrix['step name'] = self.stepMatrix['step name'].map({'a': 'add butter',
                                                                         'b': 'add sadness',
                                                                         'c': 'add sage',
                                                                         'd': 'add flour'})

        self.stepMatrix['flow name'] = self.stepMatrix['flow name'].map({'e': 'cake of destiny',
                                                                         'f': 'biscuits of fate',
                                                                         'g': 'pasta of tears',
                                                                         'h': 'bubur hitam'})

        self.arrange_steps()

        return 0

    def map_tool_count_from_csv(self, csv_link):
        self.toolCount = pd.read_csv(csv_link, index_col=0, header=0)

        return 0

    def run_bucket(self, a_loading):
        return 0

    def required_tool_of_a_time(self, moves):
        return 0
