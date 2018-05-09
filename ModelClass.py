"""

this is the main stuff here to run the bucket !!!!, and initial the date!!
"""


from WorkstationClass import Workstation
from LoadingClass import Loading
import pandas as pd
import glob
import os

# pathfile = os.path.dirname(templateFile)
# path = os.path.join(pathfile, 'aa', 'bb')

# step_matrix_path - 'modelsStorage/aStudyName/tool_step_matrix'
# load_quanti_path - 'modelsStorage/aStudyname/production_targets'
# you also need a WS util table


class Model:
    def __init__(self, study_name, major_tool_kind):
        general_link = 'modelsStorage'
        study_folder_link = os.path.join(general_link, study_name)

        self.scen_info = pd.read_csv(os.path.join(study_folder_link, 'study_information.csv'), index_col=0, header=0)
        self.scen_name = self.scen_info.at['scen_name', 'Value']
        self.loading_name = self.scen_info.at['loading_name', 'Value']
        self.model_name = self.scen_info.at['model_name', 'Value']
        self.comments = self.scen_info.at['comments', 'Value']

        list_of_links_to_tool_step_matrix = [file_name for file_name in glob.glob(
            os.path.join(study_folder_link, 'tool_step_matrix', major_tool_kind, '*.csv')
        )]

        self.link_to_loading = os.path.join(study_folder_link, 'production_targets', 'loading.csv')
        self.link_to_tool_quant = os.path.join(study_folder_link, 'tool_quan_matrix', major_tool_kind + '.csv')
        self.link_to_tool_time = os.path.join(study_folder_link, 'tool_time_matrix', major_tool_kind + '.csv')

        self.list_WS = [
            Workstation(self.link_to_tool_time, a_step_matrix, self.link_to_tool_quant)
            for a_step_matrix in list_of_links_to_tool_step_matrix
        ]

        self.loading = pd.read_csv(self.link_to_loading)
        # self.loading = Loading()
        # self.name_of_modeling =
        # self.wslist =
        # self.list_of_WS = [Workstation(x, '0.8') for x in self.list_of_WS_names]

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

        return [s for i, s in enumerate(self.list_WS) if ws_name in s.name][0]


aModel = Model('aStudyName', 'adder')
# print(aModel.link_to_tool_quant)

crazyws = aModel.ws('crazy')
# print(crazyws.stepMatrix)

crazyws.assign_moves(aModel.loading)
#print(crazyws.bucket.assigned_moves)
#print(crazyws.equip_list)
crazyws.bucket.run_assigned_moves('7/1/2018', '11/5/2018')
crazyws.bucket.plot_chart()
#print(crazyws.bucket.report.head())



# print(crazyws.bucket.report.index.values)





