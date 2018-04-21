"""

this is the loading class,and, will need to have all the projectionssssss



"""

import pandas as pd
import numpy as np


class Loading:

    def __init__(self, name, csv_link):
        self.name = name
        self.outs_target = pd.read_csv(csv_link, index_col=0, header=0)

    def update_a_loading_quantity(self, timing, product_name, quantity):
        # check if the product name is here already

        # check if timing is here

        # update
        return 0