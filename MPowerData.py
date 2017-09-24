import datetime
import json
import math
import sys


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
        self.minAcceleration = sys.float_info.max
        self.maxAcceleration = 0
        self.diffTimestampAcceleration = 0
        self.minDeviceMotion = sys.float_info.max
        self.maxDeviceMotion = 0
        self.diffTimestampDeviceMotion = 0

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
        print (self.recordId)
        print (self.healthcode)
        print (self.createdOn)
        print (self.appVersion)
        print (self.phoneInfo)
        print (self.accel_walking_outbound_file)
        print (self.deviceMotion_walking_outbound_file)
        print (self.pedometer_walking_outbound_file)
        print (self.accel_walking_return_file)
        print (self.deviceMotion_walking_return_file)
        print (self.pedometer_walking_return_file)
        print (self.accel_walking_rest_file)
        print (self.deviceMotion_walking_rest_file)
        print (self.medTimepoint)
        print ()

    def extractMinMaxDiffAcceleration(self):
        minTimeStamp = 0
        maxTimeStamp = 0
        with open (self.accel_walking_outbound_file, 'r') as f:
            array = json.load (f)

        # print(array[0])
        for i in range (len (array)):
            obj = array[i]
            totalAcceleration = math.sqrt (
                obj.get ('x') * obj.get ('x') + obj.get ('y') * obj.get ('y') + obj.get ('z') * obj.get ('z'))
            if self.minAcceleration > totalAcceleration:
                self.minAcceleration = totalAcceleration
                minTimeStamp = obj.get ('timestamp')

            if self.maxAcceleration < totalAcceleration:
                self.maxAcceleration = totalAcceleration
                maxTimeStamp = obj.get ('timestamp')

        self.diffTimestampAcceleration = maxTimeStamp - minTimeStamp
        print (self.minAcceleration)
        print (self.maxAcceleration)
        print (self.diffTimestampAcceleration)
        print ()

    # def extractMinMaxDiffDeviceMotion(self):
    #     minTimeStamp = 0
    #     maxTimeStamp = 0
    #     with open (self.deviceMotion_walking_outbound_file, 'r') as f:
    #         array = json.load (f)
    #
    #     print(self.deviceMotion_walking_outbound_file)

        # print(array[0])
        # for i in range (len (array)):
        #     obj = array[i]
        #     totalAcceleration = math.sqrt (
        #         obj.get ('x') * obj.get ('x') + obj.get ('y') * obj.get ('y') + obj.get ('z') * obj.get ('z'))
        #     if self.minDeviceMotion > totalAcceleration:
        #         self.minDeviceMotion = totalAcceleration
        #         minTimeStamp = obj.get ('timestamp')
        #
        #     if self.maxDeviceMotion < totalAcceleration:
        #         self.maxDeviceMotion = totalAcceleration
        #         maxTimeStamp = obj.get ('timestamp')
        #
        # self.diffTimestampDeviceMotion = maxTimeStamp - minTimeStamp
        # print (self.minDeviceMotion)
        # print (self.maxDeviceMotion)
        # print (self.diffTimestampDeviceMotion)
        # print ()
