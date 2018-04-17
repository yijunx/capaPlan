"""
this is the first PY file on online...
Git hub is so good


"""

import pandas as pd
import numpy as np


class Workstation:

    # def map_a_step(self, stepname, rpt, loadsize: 'use 1 for single wafer', util: 'put 0 if using WS util', inflow):
    #    self.stepMatrix.append()
    #    return 0
    def __init__(self, name, util: '0.67 for example'):
        """

        :param name:fff
        :param util:fff
        """
        self.name = name
        self.util = util
        # self.stepMatrix = pd.DataFrame(columns=['step name'])

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

    def export_to_csv(self):
        self.stepMatrix.to_csv('modelsStorage/stepMatrix.csv')
        return 0

    def map_steps_from_csv(self, csv_link):
        """

        :param csv_link:
        :return:
        """

        self.stepMatrix = pd.read_csv(csv_link, index_col=0, header=0)
        # need to check if there is duplicate combo and step/flow

        return 0

    def mass_update_a_step_name(self):
        """
        this one changes the step name in all flows
        this is a one shot file... not for any purpose
        :param old_step_name:
        :param new_step_name:
        :return:
        """
        # w['female'] = w['female'].map({'female': 1, 'male': 0})
        self.stepMatrix['step name'] = self.stepMatrix['step name'].map({'': 'add butter', '': 'add sadness',
                                                                         '': 'add sage', '': 'add flour'})

        self.stepMatrix['flow name'] = self.stepMatrix['flow name'].map({'': 'cake of destiny',
                                                                         '': 'biscuits of fate',
                                                                         '': 'pasta of tears',
                                                                         '': 'bubur hitam'})

        self.arrange_steps()

        return 0

