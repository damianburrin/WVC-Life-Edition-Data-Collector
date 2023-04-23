
import serial
from time import sleep
ser = serial.Serial ("/dev/ttyS0", 115200)


def read_data():

        received_data = ser.read()
        sleep(0.05)
        data_left = ser.inWaiting()             #check for remaining byte

        received_data += ser.read(data_left)
        return (received_data)


def format_data(data_rx):
        upload_array=[]
        data_rx=str(data_rx)
        data_rx=data_rx.split(',')
#       print(data_rx)
        if data_rx[0]=="b'AT+SENDICA=property":
#               print("found")
                if data_rx[1]=="PV_Volt":
#                       print("data found")
                        print("PV_Volt=",data_rx[2],"PV_Current=",data_rx[4],"PV_Power=",data_rx[6],"AC_Volt=",data_rx[8],"AC_Current=",data_rx[10],"Out_Power=",data_rx[12],"Temperature=",data_rx[14],"Power_adjustment=",data_rx[16],"Ene>
                        for count in range(2,20,2):
                                upload_array.append(data_rx[count])
                                print(upload_array)
#               if data_rx[1]=="PowerSwitch":
##                      print("Aux dat found!")
                        print("day energy=",data_rx[4],"Tree=",data_rx[6],"Emissions=",data_rx[8])
#                       print(data_rx)

#def upload_data(upload_array):



while True:



        data_rx = read_data()
        format_data(data_rx)
        #upload_data(upload_array)




