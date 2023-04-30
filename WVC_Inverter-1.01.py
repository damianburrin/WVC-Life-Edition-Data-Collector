#!/usr/bin/python3
import serial
from time import sleep
import requests
upload_array=[]
ser = serial.Serial ("/dev/ttyS0", 115200)

API="CONUPB0G78V8Z3HR"
# do something to auto start on pi - schedule task


def read_data():

        received_data = ser.read()
        sleep(0.3)
        data_left = ser.inWaiting()             #check for remaining byte
        received_data += ser.read(data_left)
#       ser.reset_input_buffer()
        return (received_data)


def format_data(data_rx):

        data_rx=str(data_rx)
        data_rx=data_rx.split(',')
#       print(data_rx)
        if data_rx[0]=="b'AT+SENDICA=property":
#               print("found")
                if data_rx[1]=="PV_Volt":
#                       print("data found")
                        #print("PV_Volt=",data_rx[2],"PV_Current=",data_rx[4],"PV_Power=",data_rx[6],"AC_Volt=",data_rx[8],"AC_Current=",data_rx[10],"Out_Power=",data_rx[12],"Temperature=",data_rx[14],"Power_adjustment=",data_rx[16],"En>
                        mod_last_element = data_rx[18]
                        data_rx[18] = mod_last_element[0:6] #trim the trailing mew line characters
                        for count in range(2,20,2):
                                upload_array.append(data_rx[count])
                #       print("MAIN",upload_array)


                if data_rx[1]=="PowerSwitch":

                        print("Aux dat found!")
                        if data_rx[3]=="Plant":
                                print("plant")
                        elif data_rx[3]=="Day_Energy":
                                print("Daily")
                                upload_array.append(data_rx[4])
#                               print("day energ=",data_rx[4],"Tree=",data_rx[6],"Emissions=",data_rx[8])
#                               upload_array.append(data_rx[4])
                                #print("dTA",data_rx)
#                               print("AUX,",upload_array)
#               print(len(upload_array)) #testing
                return(upload_array)

#                       print(data_rx)

def upload_data(upload_array):

#       print(len(upload_array))
#       upload data and aux data
        try:
                len(upload_array)
#
                if len(upload_array)==9:
                        url="https://api.thingspeak.com/update?api_key={7}&field1={0}&field2={1}&field3={2}&field4={3}&field5={4}&field6={5}&field7={6}".format(upload_array[0],upload_array[1],upload_array[2],upload_array[3],upload_array>
                        print("uploading data")
                        response = requests.get(url)
#                       print(response) # testing
                elif len(upload_array)==1:
                        url="https://api.thingspeak.com/update?api_key={1}&field8={0}".format(upload_array[0],API)
                        print("uploading daily")
                        response = requests.get(url)
#                       print(response) #testing
                else:
                        url="https://api.thingspeak.com/update?api_key={1}&field8={0}".format("0.01",API)
                        response = requests.get(url)
                        print("uploading 0.01")
        except:
                print("Data uplad error")
                ser.reset_input_buffer()

while True:

#do two uploads before pause
        ser.reset_input_buffer()
        sleep(0.3)
        for count in range (2):
                upload_array=[]
                data_rx = read_data()
                print(data_rx)
                upload_array=format_data(data_rx)
                print("UPLOAD",upload_array)
                upload_data(upload_array)
                ser.reset_input_buffer()
        #this is the time between uploads keep about 2 minutes  for free thingspeak account
        sleep(30)
        ser.reset_input_buffer()

