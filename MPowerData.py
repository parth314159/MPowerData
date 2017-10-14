import datetime
import json
import math
import sys
import csv
import numpy as np
import MPowerDataSet


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
        self.signalEnergyX = 0
        self.signalEnergyY = 0
        self.signalEnergyZ = 0
        self.standardDeviationPedometer = 0
        # self.minDeviceMotion = sys.float_info.max
        # self.maxDeviceMotion = 0
        # self.diffTimestampDeviceMotion = 0
        self.averageStepDistance = 0
        self.averageAccelerationResting = 0

    def parseDFRow(self, row, file_dictionary_int, file_dictionary_float):
        self.recordId = row['recordId']
        self.healthcode = row['healthCode']
        self.createdOn = row['createdOn']
        self.appVersion = row['appVersion']
        self.phoneInfo = row['phoneInfo']
        self.accel_walking_outbound_file =  file_dictionary_float.get (
            "{:.0f}".format (row['accel_walking_outbound.json.items']))
            #file_dictionary_int.get (str (row['accel_walking_outbound.json.items']))
        self.deviceMotion_walking_outbound_file = file_dictionary_float.get (
            "{:.0f}".format (row['deviceMotion_walking_outbound.json.items']))
            #file_dictionary_int.get (
            #str (row['deviceMotion_walking_outbound.json.items']))
        self.pedometer_walking_outbound_file = file_dictionary_float.get (
            "{:.0f}".format (row['pedometer_walking_outbound.json.items']))
        self.accel_walking_return_file = file_dictionary_float.get (
            "{:.0f}".format (row['accel_walking_return.json.items']))
        self.deviceMotion_walking_return_file = file_dictionary_float.get (
            "{:.0f}".format (row['deviceMotion_walking_return.json.items']))
        self.pedometer_walking_return_file = file_dictionary_float.get (
            "{:.0f}".format (row['pedometer_walking_return.json.items']))
        self.accel_walking_rest_file = file_dictionary_float.get (
            "{:.0f}".format (row['accel_walking_rest.json.items']))
            #file_dictionary_int.get (str (row['accel_walking_rest.json.items']))
        # self.deviceMotion_walking_rest_file = file_dictionary_int.get (
        #     str (row['deviceMotion_walking_rest.json.items']))
        #self.medTimepoint = row['momentInDayFormat.json.choiceAnswers']

    def printObj(self):
        print (self.recordId)
        # print (self.healthcode)
        # print (self.createdOn)
        # print (self.appVersion)
        # print (self.phoneInfo)
        print (self.accel_walking_outbound_file)
        print (self.deviceMotion_walking_outbound_file)
        print (self.pedometer_walking_outbound_file)
        print (self.accel_walking_return_file)
        print (self.deviceMotion_walking_return_file)
        print (self.pedometer_walking_return_file)
        print (self.accel_walking_rest_file)
        print (self.deviceMotion_walking_rest_file)
        # print (self.medTimepoint)
        print ()

    def extractallfeatures(self):
        #self.printObj ()
        try:
            self.extractMinMaxDiffAccelerationEnergy ()
        except ZeroDivisionError:
            pass

        try:
            self.extractAvgDistance ()
        except ZeroDivisionError:
            pass
        try:
            self.extactAverageAcceleraionResting ()
        except ZeroDivisionError:
            pass
        finally:
            self.savefeaturestocsv()

        # print ("Minimum Acceleration - ", self.minAcceleration)
        # print ("Maximum Acceleration - ", self.maxAcceleration)
        # print ("Difference Timestamp - ", self.diffTimestampAcceleration)
        # print ("Average Distance - ", self.averageStepDistance)
        # print ("Resting average acceleration - ", self.averageAccelerationResting)
        # print ("Signal energy X - ", self.signalEnergyX)
        # print ("Signal energy Y - ", self.signalEnergyY)
        # print ("Signal energy Z - ", self.signalEnergyZ)
        # print ("Pedometer Standard Deviation - ", self.standardDeviationPedometer)
        # print (self.phoneInfo)
        # print (self.medTimepoint)
        # print ()
        #self.savefeaturestocsv ()

    def extractMinMaxDiffAccelerationEnergy(self):
        if (self.accel_walking_outbound_file == None):
            return
        minTimeStamp = 0
        maxTimeStamp = 0
        x_array = []
        y_array = []
        z_array = []
        count = 0
        with open (self.accel_walking_outbound_file, 'r') as f:
            array = json.load (f)

        # print(array[0])
        for i in range (len (array)):
            obj = array[i]
            totalAcceleration = math.sqrt (
                obj.get ('x') ** 2 + obj.get ('y') ** 2 + obj.get ('z') ** 2)
            self.signalEnergyX += obj.get ('x') ** 2
            self.signalEnergyY += obj.get ('y') ** 2
            self.signalEnergyZ += obj.get ('z') ** 2
            count += 1
            if self.minAcceleration > totalAcceleration:
                self.minAcceleration = totalAcceleration
                minTimeStamp = obj.get ('timestamp')
            if self.maxAcceleration < totalAcceleration:
                self.maxAcceleration = totalAcceleration
                maxTimeStamp = obj.get ('timestamp')
        self.signalEnergyX = self.signalEnergyX / count
        self.signalEnergyY = self.signalEnergyY / count
        self.signalEnergyZ = self.signalEnergyZ / count
        self.diffTimestampAcceleration = maxTimeStamp - minTimeStamp

    def extractAvgDistance(self):
        # print(self.pedometer_walking_outbound_file)
        if (self.pedometer_walking_outbound_file == None):
            return
        PMreading = []
        array = []
        # print(self.pedometer_walking_outbound_file)
        with open (self.pedometer_walking_outbound_file, 'r') as f:
            array = json.load (f)
            if array == None:
                return

        avg_distance = 0
        count = 0

        for obj in array:
            adis = obj['numberOfSteps'] / obj['distance']
            avg_distance += adis
            PMreading.append (adis)
            count += 1
            # total_distance+=
        self.standardDeviationPedometer = np.std (PMreading)
        self.averageStepDistance = avg_distance / count

    def extactAverageAcceleraionResting(self):
        if (self.accel_walking_rest_file == None):
            return
        with open (self.accel_walking_rest_file, 'r') as f:
            array = json.load (f)
        totalAcceleration = 0
        count = 0
        # print(array[0])
        for obj in array:
            Acceleration = math.sqrt (
                obj.get ('x') * obj.get ('x') + obj.get ('y') * obj.get ('y') + obj.get ('z') * obj.get ('z'))
            totalAcceleration += Acceleration
            count += 1
        self.averageAccelerationResting = totalAcceleration / count

    def savefeaturestocsv(self):
        with open (MPowerDataSet.MPowerDataSet.table+"_MPower_features_v2.csv", "a") as csv_file:
            writer = csv.writer (csv_file, delimiter=',', lineterminator='\n')
            final = []
            final.extend ((str (self.recordId), str (self.minAcceleration), str (self.maxAcceleration),
                           str (self.diffTimestampAcceleration), str (self.averageStepDistance),
                           str (self.standardDeviationPedometer), str (self.averageAccelerationResting),
                           str (self.signalEnergyX), str (self.signalEnergyY), str (self.signalEnergyZ)))
            #print (final)
            writer.writerow (final)

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
