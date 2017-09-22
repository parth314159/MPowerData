import synapseclient
from Authenticate import Auth
from MPowerData import MPowerDTO
import warnings

class MPowerDataSet:

    def __init__(self):
        self.syn = Auth().getSynObject()
        self.table = "syn5713119"
        self.file_dictionary_int = None
        self.file_dictionary_float = None
        self.example_query = None
        self.data_frame = None
        self.dataList = []
        self.queyTableAll()
        self.saveAllfilesOffline()
        self.saveAsCSV()
        self.saveAsListObjects()

    def queyTableAll(self):
        # Query the first 10 rows and all columns of the walking training demographics table
        self.example_query = self.syn.tableQuery("SELECT * FROM "+self.table)

    def saveAsListObjects(self):
        print()
        for index, row in self.data_frame.iterrows():
            obj = MPowerDTO()
            obj.parseDFRow(row,self.file_dictionary_int,self.file_dictionary_float)
            obj.printObj()
            self.dataList.append(obj)


    def saveAsCSV(self):
        self.data_frame = self.example_query.asDataFrame()
        self.data_frame.to_csv("Dataset/"+self.table+".csv")


    def saveAllfilesOffline(self):
        warnings.filterwarnings("ignore")
        self.file_dictionary_int = dict(self.syn.downloadTableColumns(self.example_query, ['accel_walking_outbound.json.items', 'deviceMotion_walking_outbound.json.items', 'accel_walking_rest.json.items', 'deviceMotion_walking_rest.json.items']).items())
        self.file_dictionary_float = dict(self.syn.downloadTableColumns(self.example_query, [ 'pedometer_walking_outbound.json.items', 'accel_walking_return.json.items', 'deviceMotion_walking_return.json.items', 'pedometer_walking_return.json.items']).items())
        #print(self.file_dictionary_float)
