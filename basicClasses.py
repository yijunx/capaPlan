"""
this is the first PY file on online...
Git hub is so good


"""

import pandas as pd
import numpy as np


class Workstation:
    def __init__(self, name, util: '0.67 for example'):
        self.name = name
        self.util = util
        self.stepMatrix = pd.DataFrame(columns=['step name'])

    #def map_a_step(self, stepname, rpt, loadsize: 'use 1 for single wafer', util: 'put 0 if using WS util', inflow):
    #    self.stepMatrix.append()
    #    return 0

    def map_steps_from_csv(self, csv_link):
        self.stepMatrix = pd.read_csv(csv_link, header=0)
