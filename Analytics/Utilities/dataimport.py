import pandas as pd
import numpy as np
import re
import glob
"""
data utlity import functions
combine csvs in a directory and concat into one, very basic

"""


class ImportData:
    def __init__(self,directory):
        self.directory = directory

    def combineCSV(self):
        filenames = glob.glob(self.directory + "/*.csv")
        li = []
        for filename in filenames:
            df = pd.read_csv(filename, index_col=None, header=0)
            li.append(df)
        frame = pd.concat(li, axis=0, ignore_index=True)
        return frame
