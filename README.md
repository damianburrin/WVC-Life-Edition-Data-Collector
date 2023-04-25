# WVC-Life-Edition-Data-Collector
A project to get better data analysis from the WVC R3 Life edition inverters. (Currently tested on the WVC700 R3 Life Edition)

Current understandsing

The LIFE edition seems to have no connection to the UART for command input - i'm sure there is as you can power down and change the power limits remotely but i didn't look to hard as i only wanted to log the data.

It makes a connection to the WIFI and It's server (alicloud) 

<b>+ILOPCONNECT=WIFI_CONNECT</br>
+ILOPCONNECT=SERVER_CONNECT</b>

It Then sends a cycled serial connection on a permentent loop

First this</br>
<b>
AT+SENDICA=property,PV_Volt,50.8,PV_Current,1.09,PV_Power,55.4,AC_Volt,243.2,AC_Current,0.20,Out_Power,51.0,Temperature,30.0,Power_adjustment,100,Energy,94.89
+ok<br></br>
</b>
Then this</br>
<b>
AT+SENDICA=property,PowerSwitch,1,Plant,0.16,Emission,0.09,Time,30,P_adj,66,TEMP_SET,67
+ok
</b></br><br>
or this</br>

<b>
AT+SENDICA=property,PowerSwitch,1,Daily,0.10,Plant,0.16,Emission,0.09,Time,30,P_adj,66,TEMP_SET,67
+ok</br></br>
</b>
<p>For some reason, Which I haven't got my head round, sometimes it included the Daily energy before the Plant (Trees) in the second send - it might only send it when this is greater than 0.01 but its a strange one i've written round to be sure i don't through an error and only upload the daily if its there</p>

Initialy I tapped the UART with an open logger and collected the data to a text file on a sdcard to see what I have
The first versions of the python script read this data from a copy of the text file and then formats the data to be processesed before uploading to ThinkSpeak.

I've  added a 2 min delay as this simulated how often i would normally send to make sure the free thinkspeak update limits are met

Implementing The Pi

Using a Pi Zero (Wifi edition) I've taken the tap for the open logger and transfer the + to the 5v in Pin 4, Ground to Pin 6 and TX to the UART RX GPIO 15 pin 10.  Even though its 3.3 volts  coming from the UART of the inverter this is enough to power the PiZero and handle the load.  I've not connected anything from the TX pin of the PI as i've no need to write back at this point


To Do
Store all the data collected in a slqlite database so this can be accessed and analyised sperately
fix upload error
auto start up script as a cron job

To Use
Register with a free ThingSpeak account - a free account is enough requests for between 2 and 4 minutes upload schedule.  I'll be setting mine to 5 minutes

![image](https://user-images.githubusercontent.com/18092613/233067232-51e05831-b3dd-4651-9f8d-82283e4708a2.png)

Set up your fields to match the image below

![image](https://user-images.githubusercontent.com/18092613/233067452-5f0564bc-e5bf-4e0e-8cfc-6b77060c2096.png)

Congigure your graphs - see my example.  THis is up to you really.  
![image](https://user-images.githubusercontent.com/18092613/233067629-367b6bb4-da00-4a8c-bce7-14bc63fc9550.png)

