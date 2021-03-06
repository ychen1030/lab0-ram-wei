
#####################################################################################
#
#  Copyright (c) 2016 Eric Burger, Wallflower.cc
#
#  MIT License (MIT)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
#####################################################################################

'''
 In this example, we will create an object (test-object) and a stream
 (test-stream) and populate it with random values.
'''
import requests
import json
import random
import time
import datetime
import ReceiveDatatest

base = 'http://127.0.0.1:5000'
network_id = 'local'
header = {}

#Test Code
#Create connection with Test Object
query_sensor = {
    'object-name': 'Sensor Reading'
}
query_button = {
    'object-name': 'Button State'
}
query_report = {
    'object-name' : 'Report State'
}

#Part1
 #Create new connection with car objects to store data obtained from
 #MyGreenCar metamodel
query_leaf_co2 = {
    'object-name': 'MyGreenCar Emission'
}
query_leaf_cost = {
    'object-name': 'MyGreenCar Cost'
}
query_camry_co2 = {
    'object-name': 'MyGreenCar Emission'
}
query_camry_cost = {
    'object-name': 'MyGreenCar Cost'
}
query_model-s_co2 = {
    'object-name': 'MyGreenCar Emission'
}
query_model-s_cost = {
    'object-name': 'MyGreenCar Cost'
}
query_crv_co2 = {
    'object-name': 'MyGreenCar Emission'
}
query_crv_cost = {
    'object-name': 'MyGreenCar Cost'
}
query_bmw_co2 = {
    'object-name': 'MyGreenCar Emission'
}
query_bmw_cost = {
    'object-name': 'MyGreenCar Cost'
}
query_analysis-a_report = {
    'object-name' : 'Report State'
}
query_analysis-b_report = {
    'object-name' : 'Report State'
}
query_analysis-c_report = {
    'object-name' : 'Report State'
}

#Test code
endpoint_sensor = '/networks/'+network_id+'/objects/sensorreading'
endpoint_button = '/networks/'+network_id+'/objects/buttonstate'
endpoint_report = '/networks/'+network_id+'/objects/test-object'

#MyGreenCar metamodel data
#Create connection to the endpoints
endpoint_leaf_co2 = '/networks/'+network_id+'/objects/sensorreading'
endpoint_leaf_cost = '/networks/'+network_id+'/objects/buttonstate'
endpoint_camry_co2 = '/networks/'+network_id+'/objects/test-object'
endpoint_camry_cost = '/networks/'+network_id+'/objects/sensorreading'
endpoint_model-s_co2 = '/networks/'+network_id+'/objects/buttonstate'
endpoint_model-s_cost = '/networks/'+network_id+'/objects/test-object'
endpoint_crv_co2 = '/networks/'+network_id+'/objects/sensorreading'
endpoint_crv_cost = '/networks/'+network_id+'/objects/buttonstate'
endpoint_bmw_co2 = '/networks/'+network_id+'/objects/test-object'
endpoint_bmw_cost = '/networks/'+network_id+'/objects/sensorreading'
endpoint_analysis-a = '/networks/'+network_id+'/objects/buttonstate'
endpoint_analysis-b = '/networks/'+network_id+'/objects/test-object'
endpoint_analysis-c = '/networks/'+network_id+'/objects/test-object'

#Test code
response_sensor = requests.request('PUT', base + endpoint_sensor, params=query_sensor, headers=header, timeout=120 )
response_button = requests.request('PUT', base + endpoint_button, params=query_button, headers=header, timeout=120 )
response_report = requests.request('PUT', base + endpoint_button, params=query_report, headers=header, timeout=120 )

#MyGreenCar metamodel data
#Push data to the endpoints
response_leaf_co2 = requests.request('PUT', base + endpoint_leaf_co2, params=query_leaf_co2, headers=header, timeout=120 )
response_leaf_cost = requests.request('PUT', base + endpoint_leaf_cost, params=query_leaf_cost, headers=header, timeout=120 )
response_camry_co2 = requests.request('PUT', base + endpoint_camry_co2, params=query_camry_co2, headers=header, timeout=120 )
response_camry_cost = requests.request('PUT', base + endpoint_camry_cost, params=query_camry_cost, headers=header, timeout=120 )
response_model-s_co2 = requests.request('PUT', base + endpoint_model-s_co2, params=query_model-s_co2, headers=header, timeout=120 )
response_model-s_cost = requests.request('PUT', base + endpoint_model-s_cost, params=query_model-s_cost, headers=header, timeout=120 )
response_crv_co2 = requests.request('PUT', base + endpoint_crv_co2, params=query_crv_co2, headers=header, timeout=120 )
response_crv_cost = requests.request('PUT', base + endpoint_crv_cost, params=query_crv_cost, headers=header, timeout=120 )
response_bmw_co2 = requests.request('PUT', base + endpoint_bmw_co2, params=query_bmw_co2, headers=header, timeout=120 )
response_bmw_cost = requests.request('PUT', base + endpoint_bmw_cost, params=query_bmw_cost, headers=header, timeout=120 )
response_analysis-a = requests.request('PUT', base + endpoint_analysis-a, params=query_analysis-a_report, headers=header, timeout=120 )
response_analysis-b = requests.request('PUT', base + endpoint_analysis-b, params=query_analysis-b_report, headers=header, timeout=120 )
response_analysis-c = requests.request('PUT', base + endpoint_analysis-c, params=query_analysis-c_report, headers=header, timeout=120 )

#Test code make sure data has been posted, if not spit an error
resp_sensor = json.loads( response_sensor.text )
resp_button = json.loads( response_button.text )
resp_report = json.loads (response_report.text )
#Trouble shoot the obtention of the data
if resp_sensor['object-code'] == 201:
    print('Create object sensorreading: ok')
else:
    print('Create object sensorreading: error')
    print( response_sensor.text )

if resp_button['object-code'] == 201:
    print('Create object buttonstate: ok')
else:
    print('Create object buttonstate: error')
    print( response_button.text )

if resp_report['object-code'] == 201:
    print('Create object buttonstate: ok')
else:
    print('Create object buttonstate: error')
    print( response_report.text )


query_sensor = {
    'stream-name': 'Sensor Stream',
    'points-type': 'i' # 'i', 'f', or 's'
}
query_button = {
    'stream-name': 'Button Stream',
    'points-type': 'i' # 'i', 'f', or 's'
}

query_report = {
    'stream-name': 'Button Stream',
    'points-type': 'i' # 'i', 'f', or 's'
}

endpoint_sensor = '/networks/'+network_id+'/objects/sensorreading/streams/stm-sensor'
response_sensor = requests.request('PUT', base + endpoint_sensor, params=query_sensor, headers=header, timeout=120 )
resp_sensor = json.loads( response_sensor.text )

endpoint_button = '/networks/'+network_id+'/objects/buttonstate/streams/stm-button'
response_button = requests.request('PUT', base + endpoint_button, params=query_button, headers=header, timeout=120 )
resp_button = json.loads( response_button.text )

endpoint_report = '/networks/'+network_id+'/objects/test-object/streams/test-stream'
response_report = requests.request('PUT', base + endpoint_button, params=query_report, headers=header, timeout=120 )
resp_report = json.loads( response_report.text )

if resp_sensor['stream-code'] == 201:
    print('Create stream stm-sensor: ok')
else:
    print('Create stream stm-sensor: error')
    print( response_sensor.text )

if resp_button['stream-code'] == 201:
    print('Create stream stm-button: ok')
else:
    print('Create stream stm-button: error')
    print( response_button.text )

if resp_report['stream-code'] == 201:
    print('Create stream stm-button: ok')
else:
    print('Create stream stm-button: error')
    print( response_report.text )

print("Start sending random points (Ctrl+C to stop)")
endpoint_sensor = '/networks/local/objects/sensorreading/streams/stm-sensor/points'
endpoint_button = '/networks/local/objects/buttonstate/streams/stm-button/points'
endpoint_report = '/networks/local/objects/test-object/streams/test-stream/points'

while True:
    ArduinoReading = ReceiveDatatest.loop()
    TypeReading = type(ArduinoReading)

    if isinstance(ArduinoReading,str):
        if ArduinoReading == "y":
            query_button = {
                'points-value': 0,
                'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            }
            print query_button

        elif ArduinoReading =="n":
            query_button = {
                'points-value': 1,
                'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            }
            print query_button
        else:
            print "false reading"

    elif isinstance(ArduinoReading,int):
        if ArduinoReading != 0:
            print ("I made it here")
            ArduinoReading_percentage = 100-(ArduinoReading*100)/255
            query_sensor = {
                'points-value': ArduinoReading,
                'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                }
            print query_sensor
            query_report = {
                'points-value': ArduinoReading_percentage,
                'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                }
            print query_report
        else:
            print "Wrong data reading"
    else:
        print "Empty reading"

    response_sensor = requests.request('POST', base + endpoint_sensor, params=query_sensor, headers=header, timeout=120 )
    response_button = requests.request('POST', base + endpoint_button, params=query_button, headers=header, timeout=120 )
    response_report = requests.request('POST', base + endpoint_report, params=query_report, headers=header, timeout=120 )
    resp_sensor = json.loads( response_sensor.text )
    resp_button = json.loads( response_button.text )
    resp_report = json.loads( response_report.text )
    if resp_sensor['points-code'] == 200:
        print( 'Update resp_sensor points: ok')
    else:
        print( 'Update resp_sensor points: error')
        print( response_sensor.text )

    if resp_button['points-code'] == 200:
        print( 'Update resp_button points: ok')
    else:
        print( 'Update resp_button points: error')
        print( response_button.text )

    if resp_report['points-code'] == 200:
        print( 'Update resp_button points: ok')
    else:
        print( 'Update resp_button points: error')
        print( response_report.text )
    time.sleep(10)
