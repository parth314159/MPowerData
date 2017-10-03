import synapseclient
from Authenticate import Auth
from MPowerData import MPowerDTO
import warnings
import csv

class MPowerDataSet:

    table = "syn10146553"

    def __init__(self):
        self.syn = Auth().getSynObject()
        self.file_dictionary_int = None
        self.file_dictionary_float = None
        self.example_query = None
        self.data_frame = None
        self.dataList = []

        with open(MPowerDataSet.table+"_MPower_features.csv", "w") as outcsv:
            writer = csv.writer(outcsv, lineterminator='\n')
            writer.writerow(["recordId", "Feature1", "Feature2", "Feature3", "Feature4", "Feature5", "Feature6", "Feature7", "Feature8" , "Feature9", "medTimePoint"])

        self.queyTableAll()
        self.saveAllfilesOffline()
        self.saveAsCSV()
        self.saveAsListObjects()


    def queyTableAll(self):
        # Query the first 10 rows and all columns of the walking training demographics table
        self.example_query = self.syn.tableQuery("SELECT * FROM "+MPowerDataSet.table)

    def saveAsListObjects(self):
        print()
        for index, row in self.data_frame.iterrows():
            obj = MPowerDTO()
            obj.parseDFRow(row,self.file_dictionary_int,self.file_dictionary_float)
            #obj.printObj()
            self.dataList.append(obj)
            obj.extractallfeatures()
            # obj.extractMinMaxDiffDeviceMotion()

    def saveAsCSV(self):
        self.data_frame = self.example_query.asDataFrame()
        self.data_frame.to_csv("Dataset/"+self.table+".csv")


    def saveAllfilesOffline(self):
        #warnings.filterwarnings("ignore")
        try:
            self.file_dictionary_int = dict(self.syn.downloadTableColumns(self.example_query, 'accel_walking_outbound.json.items').items())

            self.file_dictionary_int = dict(self.syn.downloadTableColumns(self.example_query,'accel_walking_rest.json.items').items())

            #self.file_dictionary_float = dict(self.syn.downloadTableColumns(self.example_query, [ 'pedometer_walking_outbound.json.items', 'accel_walking_return.json.items', 'deviceMotion_walking_return.json.items', 'pedometer_walking_return.json.items']).items())

            self.file_dictionary_float = dict(self.syn.downloadTableColumns(self.example_query, 'pedometer_walking_outbound.json.items').items())
            #print(self.file_dictionary_float)
        except synapseclient.exceptions.SynapseTimeoutError:
            self.saveAllfilesOffline()
