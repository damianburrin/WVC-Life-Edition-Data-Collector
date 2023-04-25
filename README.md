# WVC (Life Edition) Data Collector
A project to get better data analysis from the WVC R3 Life edition inverters. (Currently tested on the WVC700 R3 Life Edition)
![Inked20230415_133150_LI](https://user-images.githubusercontent.com/18092613/234235327-2c00d303-561b-4173-b354-c25f6d245ed6.jpg)

![20230415_133114](https://user-images.githubusercontent.com/18092613/234233316-eb3c3f2d-cd98-4a34-8e79-3b9246bc3d0d.jpg)

<b>Current understandsing</b>
<p>The Wifi chip is a HF-LPT270 and fairly well documented online http://www.hi-flying.com/hf-lpt270 and here https://manuals.plus/m/5176309d280b9892c2bce6f24685fa4b934f7f79a321716bc0bc6c0f4dfe03bf_optim.pdf
</p>

![PINS](https://user-images.githubusercontent.com/18092613/234236983-367b608f-5a6a-4150-9e70-705137ed0e23.jpg)

<br>
The LIFE edition seems to have no connection from the UART to the J4 header on the board- i'm sure the UART takes and input in as you can power down and change the power limits remotely via the cloud intelligence app but i didn't look to hard as i only wanted to log the data.

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
<p>For some reason, which I haven't got my head round, sometimes it included the Daily energy before the Plant (Trees) in the second send - it might only send it when this is greater than 0.01 but its a strange one i've written round to be sure i don't through an error and only upload the daily if its there</p>

Initialy I tapped the UART with an open logger and collected the data to a text file on a sdcard to see what I have
The first versions of the python script read this data from a copy of the text file and then formats the data to be processesed before uploading to ThinkSpeak.
![Inked20230415_133328_LI](https://user-images.githubusercontent.com/18092613/234235022-c4843dd2-7ab7-402a-93a3-801890a17e90.jpg)

I've  added a 2 min delay as this simulated how often i would normally send to make sure the free thinkspeak update limits are met

<b>Implementing The Pi</b>

Using a Pi Zero (Wifi edition) I've taken the tap for the open logger and transfer the + to the 5v in Pin 4, Ground to Pin 6 and TX to the UART RX GPIO 15 pin 10.  Even though its 3.3 volts  coming from the UART of the inverter this is enough to power the PiZero and handle the load.  I've not connected anything from the TX pin of the PI as i've no need to write back at this point


<b>To Do</b>
Store all the data collected in a slqlite database so this can be accessed and analyised sperately
fix upload error
auto start up script as a cron job

<b>To Use</b>
Register with a free ThingSpeak account - a free account is enough requests for between 2 and 4 minutes upload schedule.  I'll be setting mine to 5 minutes

![image](https://user-images.githubusercontent.com/18092613/233067232-51e05831-b3dd-4651-9f8d-82283e4708a2.png)

Set up your fields to match the image below

![image](https://user-images.githubusercontent.com/18092613/233067452-5f0564bc-e5bf-4e0e-8cfc-6b77060c2096.png)

Congigure your graphs - see my example.  THis is up to you really.  
![image](https://user-images.githubusercontent.com/18092613/233067629-367b6bb4-da00-4a8c-bce7-14bc63fc9550.png)

