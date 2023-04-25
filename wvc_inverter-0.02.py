
import serial
from time import sleep
ser = serial.Serial ("/dev/ttyS0", 115200)


def read_data():

        received_data = ser.read()
        sleep(0.05)
        data_left = ser.inWaiting()             #check for remaining byte

        received_data += ser.read(data_left)
        return (received_data)

def sendData(values):

    url="https://api.thingspeak.com/update?api_key=APIGOESHERE&field1={0}&field2={1}&field3={2}&field4={3}&field5={4}&field6={5}&field7={6}".format(values[0],values[1],values[2],values[3],values[4],values[5],values[8])
    response = requests.get(url)    
    print(values)


def format_data(data_rx):
        data=data_rx.split(',')
        print(data)

def process_data(data_rx):
    if data_rx[0]=="b'AT+SENDICA=property":
        #print("found")
        if data_rx[1]=="PV_Volt":
            print("data")
            print("PV_Volt=",data_rx[2],"PV_Current=",data_rx[4],"PV_Power=",data_rx[6],"AC_Volt=",data_rx[8],"AC_Current=",data_rx[10],"Out_Power=",data_rx[12],
                  "Temperature=",data_rx[14],"Power_adjustment=",data_rx[16],"Energy=",data_rx[18])
        if data_rx[1]=="PowerSwitch":
            print("aux data")
            print("PowerSwitch=",x[2],"Plant=",x[4],"Emission=",x[6])
            
    

while True:
        data_rx = read_data()
        data_rx=str(data_rx)
        data_rx=data_rx.split(',')

        #print(data_rx[1])


               """  values=[]
                 values.append(x[2])
                 values.append(x[4])
                 values.append(x[6])
                 values.append(x[8])
                 values.append(x[10])
                 values.append(x[12])
                 values.append(x[14])
                 values.append(x[16])
                 values.append(x[18])
                 print("\n\nsending",values)
                # sendData(values)
                # time.sleep(120)"""
                 
                 


