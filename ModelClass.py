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
        return 0

    def dup_a_model(self):
        return 0

    def update_scen_info(self):
        return 0


aModel = Model('modelsStorage/aStudyName')
print(aModel.comments)
print(aModel.list_of_WS_names)






