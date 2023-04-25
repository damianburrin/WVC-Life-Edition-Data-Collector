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

                if data_rx[1]=="PowerSwitch" and data_rx[4]=="day energy=":

##                      print("Aux dat found!")
#                       print("day energy=",data_rx[4],"Tree=",data_rx[6],"Emissions=",data_rx[8])
                        upload_array.append(data_rx[4])
                        #print("dTA",data_rx)
#                       print("AUX,",upload_array)
                return(upload_array)

#                       print(data_rx)

def upload_data(upload_array):

#       print(len(upload_array))
#       upload data and aux data
        if len(upload_array)==9:
                url="https://api.thingspeak.com/update?api_key={7}&field1={0}&field2={1}&field3={2}&field4={3}&field5={4}&field6={5}&field7={6}".format(upload_array[0],upload_array[1],upload_array[2],upload_array[3],upload_array[4],uplo>
                response = requests.get(url)
        elif len(upload_array)==1:
                url="https://api.thingspeak.com/update?api_key={1}&field8={0}".format(upload_array[0],API)
                response = requests.get(url)
while True:

#do two uploads before pause
        for count in range (2):
                upload_array=[]
                data_rx = read_data()
                print("raw data",data_rx)
                upload_array=format_data(data_rx)
                print("UPLOAD",upload_array)
                upload_data(upload_array)
        #this is the time between uploads keep above 2 minutes  for free thingspeak account
        sleep(300)







