"""



this is a class that shapes the necesarry information of a class


"""


class ScenInfo:
    def __init__(self, name, csv_study_dir):
        self.name = name
        self.link = csv_study_dir

        # l = [pd.read_csv(filename) for filename in glob.glob("/path/*.txt")]
        # df = pd.concat(l, axis=0)