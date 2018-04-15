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

        :param name:
        :param util:
        """
        self.name = name
        self.util = util
        self.stepMatrix = pd.DataFrame(columns=['step name'])

    #def map_a_step(self, stepname, rpt, loadsize: 'use 1 for single wafer', util: 'put 0 if using WS util', inflow):
    #    self.stepMatrix.append()
    #    return 0

    def map_steps_from_csv(self, csv_link):
        """

        :param csv_link:
        :return:
        """
        self.stepMatrix = pd.read_csv(csv_link, header=0)
        return 0

    def update_steps(self, step_name, in_flow: 'pull ALL for all flows', what_to_change: 'put rpt/ls/util', new_value):
        """
        this updated steps can add step as well, it will detect whether the step flow combo is in the current setting
        :param step_name: a
        :param in_flow: a
        :param what_to_change: please use a list, can put ['rpt','ls']
        :param new_value: eg: ['350','125']
        :return:
        """
        #check if the step_name/in_flow combo is new or existing in the matrix
        if ((aWS.stepMatrix['step name'] == step_name) & (aWS.stepMatrix['flow name'] == in_flow)).any():
            targetIndex = self.stepMatrix.loc[(aWS.stepMatrix['step name'] == step_name) & (aWS.stepMatrix['flow name'] == in_flow)].index
            self.stepMatrix.set_value(targetIndex,'rpt',)


        else:
            #the step is not in there, hence this is a new step



        #self.stepMatrix.set_value(self.stepMatrix.loc[])
        return 0
    def add_steps(self):
        """

        :return:
        """
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
