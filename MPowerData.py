import datetime


class MPowerDTO:
    def __init__(self, recordId="", healthcode="", createdOn="", appVersion="", phoneInfo="",
                 accel_walking_outbound_file="", deviceMotion_walking_outbound_file="",
                 pedometer_walking_outbound_file="", accel_walking_return_file="", deviceMotion_walking_return_file="",
                 pedometer_walking_return_file="", accel_walking_rest_file="", deviceMotion_walking_rest_file="",
                 medTimepoint=""):
        self.recordId = recordId
        self.healthcode = healthcode
        self.createdOn = createdOn
        self.appVersion = appVersion
        self.phoneInfo = phoneInfo
        self.accel_walking_outbound_file = accel_walking_outbound_file
        self.deviceMotion_walking_outbound_file = deviceMotion_walking_outbound_file
        self.pedometer_walking_outbound_file = pedometer_walking_outbound_file
        self.accel_walking_return_file = accel_walking_return_file
        self.deviceMotion_walking_return_file = deviceMotion_walking_return_file
        self.pedometer_walking_return_file = pedometer_walking_return_file
        self.accel_walking_rest_file = accel_walking_rest_file
        self.deviceMotion_walking_rest_file = deviceMotion_walking_rest_file
        self.medTimepoint = medTimepoint

    def parseDFRow(self, row, file_dictionary_int, file_dictionary_float):
        self.recordId = row['recordId']
        self.healthcode = row['healthCode']
        self.createdOn = row['createdOn']
        self.appVersion = row['appVersion']
        self.phoneInfo = row['phoneInfo']
        self.accel_walking_outbound_file = file_dictionary_int.get (str (row['accel_walking_outbound.json.items']))
        self.deviceMotion_walking_outbound_file = file_dictionary_int.get (
            str (row['deviceMotion_walking_outbound.json.items']))
        self.pedometer_walking_outbound_file = file_dictionary_float.get (
            str (row['pedometer_walking_outbound.json.items']).rstrip ('.0'))
        self.accel_walking_return_file = file_dictionary_float.get (
            str (row['accel_walking_return.json.items']).rstrip ('.0'))
        self.deviceMotion_walking_return_file = file_dictionary_float.get (
            str (row['deviceMotion_walking_return.json.items']).rstrip ('.0'))
        self.pedometer_walking_return_file = file_dictionary_float.get (
            str (row['pedometer_walking_return.json.items']).rstrip ('.0'))
        self.accel_walking_rest_file = file_dictionary_int.get (str (row['accel_walking_rest.json.items']))
        self.deviceMotion_walking_rest_file = file_dictionary_int.get (
            str (row['deviceMotion_walking_rest.json.items']))
        self.medTimepoint = row['medTimepoint']


    def printObj(self):
        print(self.recordId)
        print(self.healthcode)
        print(self.createdOn)
        print(self.appVersion)
        print(self.phoneInfo)
        print(self.accel_walking_outbound_file)
        print(self.deviceMotion_walking_outbound_file)
        print(self.pedometer_walking_outbound_file)
        print(self.accel_walking_return_file)
        print(self.deviceMotion_walking_return_file)
        print(self.pedometer_walking_return_file)
        print(self.accel_walking_rest_file)
        print(self.deviceMotion_walking_rest_file)
        print(self.medTimepoint)
        print()
