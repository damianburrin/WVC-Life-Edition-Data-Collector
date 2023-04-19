# WVC-Life-Edition-Data-Collector
A project to get better data analysis from the WVC R3 Life edition inverters.

Current understandsing

The LIFE edition seems to have no connection to the UART for command input
It makes a connection to the WIFI and It's server (alicloud) and then sends two data streams ever two minutes.  

+ILOPCONNECT=WIFI_CONNECT
+ILOPCONNECT=SERVER_CONNECT


AT+SENDICA=property,PV_Volt,50.8,PV_Current,1.09,PV_Power,55.4,AC_Volt,243.2,AC_Current,0.20,Out_Power,51.0,Temperature,30.0,Power_adjustment,100,Energy,94.89
+ok
AT+SENDICA=property,PowerSwitch,1,Plant,0.16,Emission,0.09,Time,30,P_adj,66,TEMP_SET,67
+ok

Current i've tapped the UArt with an open logger and collect the data to a text file on a sdcard to see what I have
The current python script reads this data from a copy of the text file and then formats the data to be processesed before uploading to ThinkSpeak

I've currently added a 2 min delay as this is how often it would normally send to simulate this and makes sure the free thinkspeak update limits are met

Next steps
Store all the data collected in a slqlite database so this can be accessed and analyised sperately
Tap the serial UART directly to a GPIO input on a pi so the data is automatically uploaded without the need to manually remove and SD card
Calcualte the daily energy collected as only the total energy is acutally sent

Register with a free ThingSpeak account - a free account is enough requests for the 2min per day upload done by the inverter

![image](https://user-images.githubusercontent.com/18092613/233067232-51e05831-b3dd-4651-9f8d-82283e4708a2.png)

Set up your fields

![image](https://user-images.githubusercontent.com/18092613/233067452-5f0564bc-e5bf-4e0e-8cfc-6b77060c2096.png)

Congigure your graphs
![image](https://user-images.githubusercontent.com/18092613/233067629-367b6bb4-da00-4a8c-bce7-14bc63fc9550.png)

