"""

this is the main stuff here to run the bucket !!!!, and initial the date!!
"""


from WorkstationClass import Workstation
from LoadingClass import Loading
import pandas as pd
import glob
import os


# step_matrix_path - 'modelsStorage/aStudyName/ws_step_matrix'
# load_quanti_path - 'modelsStorage/aStudyname/loadings_storage'
# you also need a WS util table

class Model:
    def __init__(self, model_folder_link):
        self.scen_info = pd.read_csv(model_folder_link + '/scen_info.csv', index_col=0, header=0)
        self.scen_name = self.scen_info.at['scen_name', 'Value']
        self.loading_name = self.scen_info.at['loading_name', 'Value']
        self.model_name = self.scen_info.at['model_name', 'Value']
        self.comments = self.scen_info.at['comments', 'Value']
        self.list_of_WS_links = [filename for filename in glob.glob(model_folder_link + '/ws_step_matrix/*.csv')]
        self.list_of_WS_names = [os.path.split(x)[1][:-4] for x in self.list_of_WS_links]
        # self.loading = Loading()
        # self.name_of_modeling =
        # self.wslist =
        self.list_of_WS = [Workstation(x, '0.8') for x in self.list_of_WS_names]

    def run_bucket(self):
        """
        this code assign loading to each WS...
        which is a bit hardddd
        how sure how to do shared ws stuffff
        well ummm, this is the core portion of the whole thing

        this portion should be able to first detect workstation group, then do balance all the time maybe
        need to have all the weekly information ready at the first stages of this portion

        then based on the ws attribute..
        mmmm


        :return:
        """
        return 0

    def dup_a_model(self):
        return 0

    def update_scen_info(self):
        return 0

    def ws(self, ws_name):
        """


        :param ws_name: some keywards of the ws name, not exact match also ok
        :return: return the WS object
        """
        index_of_ws = [i for i, s in enumerate(self.list_of_WS_names) if ws_name in s][0]
        return self.list_of_WS[index_of_ws]


aModel = Model('modelsStorage/aStudyName')
print(aModel.comments)
print(aModel.list_of_WS_names)
print(aModel.ws('baker').name)






