"""


this file is to manage the flow, like cycle time etc etc
this flow information, does not contain ws, it onlys has step sequence and cycle time to outs
the mapping information is the WS matrix

"""

import pandas as pd
import numpy as np


class Flow:

    def __init__(self, name, csv_link):
        self.name = name
        self.outs_target = pd.read_csv(csv_link, index_col=0, header=0)

    def update_a_loading_quantity(self, timing, product_name, quantity):
        # check if the product name is here already

        # check if timing is here

        # update
        return 0

