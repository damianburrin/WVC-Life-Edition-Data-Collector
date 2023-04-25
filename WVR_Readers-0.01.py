import requests
import time
mf = open("LOG00092.TXT", "r+")
print("File to read: ", mf.name)


def sendData(values):
    #apikey
    #api="CONUPB0G78V8Z3HR"
    #host="api.thingspeak.com"
    #conn_open_tcp(host, 80)
    url="https://api.thingspeak.com/update?api_key=API&field1={0}&field2={1}&field3={2}&field4={3}&field5={4}&field6={5}&field7={6}".format(values[0],values[1],values[2],values[3],values[4],values[5],values[8])
    response = requests.get(url)
    
    #response = requests.get("""GET /update?api_key={0}&field1={2}&field2={3}&field3={4}&field4={5} HTTP/1.0\r\n Host: {1}\r\nConnection: close\r\n\r\n""".format(api,host,values[0],values[1],values[2],values[3]))
    print(values) 

# Read single line in file
file_line = mf.readline()


# use the readline() method to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty

while file_line:
    x=file_line.split(',')
    #print(x[0])
    if x[0]=="AT+SENDICA=property":
         if x[1]=="PV_Volt":
             print("data")
             print("PV_Volt=",x[2],"PV_Current=",x[4],"PV_Power=",x[6],"AC_Volt=",x[8],"AC_Current=",x[10],"Out_Power=",x[12],
                   "Temperature=",x[14],"Power_adjustment=",x[16],"Energy=",x[18])

             values=[]
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
             sendData(values)
             time.sleep(120)
             
             
         if x[1]=="PowerSwitch":
             print("aux data")
             print("PowerSwitch=",x[2],"Plant=",x[4],"Emission=",x[6])
             
             
             



    # use readline() to read next line
    file_line = mf.readline()


# Close opened file
mf.close()



       


