"""
this is the first PY file on online...
Git hub is so good


"""

import pandas as pd
import numpy as np
import datetime


class Workstation:
    def __init__(self, name, util: '0.67 for example'):
        """

        :param name:fff
        :param util:fff
        """
        self.name = name
        self.util = util
        self.stepMatrix = pd.DataFrame(columns=['step name'])

    # def map_a_step(self, stepname, rpt, loadsize: 'use 1 for single wafer', util: 'put 0 if using WS util', inflow):
    #    self.stepMatrix.append()
    #    return 0

    def map_steps_from_csv(self, csv_link):
        """

        :param csv_link:
        :return:
        """

        self.stepMatrix = pd.read_csv(csv_link, header=0)
        # need to check if there is duplicate combo and step/flow

        return 0

    def update_a_step(self,
                      step_name,
                      in_flow: 'pull ALL for all flows',
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
        if ((self.stepMatrix['step name'] == step_name) & (self.stepMatrix['flow name'] == in_flow)).any():
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

        # then arrange
        self.arrange_steps()
        return 0

    def remove_steps(self):
        """

        :return:
        """
        return 0

    def arrange_steps(self):
        """

        :return:
        """
        return 0

    def delete_column_in_matrix(self, column_name):
        """

        :param column_name:
        :return:
        """
        return 0
