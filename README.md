# WVC (Life Edition) Data Collector
A project to get better data analysis from the WVC R3 Life edition inverters. (Currently tested on the WVC700 R3 Life Edition)
![Inked20230415_133150_LI](https://user-images.githubusercontent.com/18092613/234235327-2c00d303-561b-4173-b354-c25f6d245ed6.jpg)

![20230415_133114](https://user-images.githubusercontent.com/18092613/234233316-eb3c3f2d-cd98-4a34-8e79-3b9246bc3d0d.jpg)

<b>Current understandsing</b>
<p>The Wifi chip is a HF-LPT270 and fairly well documented online http://www.hi-flying.com/hf-lpt270 and here https://manuals.plus/m/5176309d280b9892c2bce6f24685fa4b934f7f79a321716bc0bc6c0f4dfe03bf_optim.pdf
</p>

![PINS](https://user-images.githubusercontent.com/18092613/234236983-367b608f-5a6a-4150-9e70-705137ed0e23.jpg)

<br>
The LIFE edition seems to have no connection from the UART RX to the J4 header on the board- i'm sure the UART takes an input in as you can power down and change the power limits remotely via the cloud intelligence app but i didn't look to hard as i only wanted to log the data.

<p></br>It first makes a connection to the WIFI and It's server (alicloud) on power up</br></p>

<b>+ILOPCONNECT=WIFI_CONNECT</br>
+ILOPCONNECT=SERVER_CONNECT</b>

It Then sends a cycled serial connection on a permentent loop - the order is set but is really dependent on where you are in the sequence when you start the python script.

The Main data is sent</br>
<b>
AT+SENDICA=property,PV_Volt,50.8,PV_Current,1.09,PV_Power,55.4,AC_Volt,243.2,AC_Current,0.20,Out_Power,51.0,Temperature,30.0,Power_adjustment,100,Energy,94.89
+ok<br></br>
</b>
And then this additional data</br>
<b>
AT+SENDICA=property,PowerSwitch,1,Plant,0.16,Emission,0.09,Time,30,P_adj,66,TEMP_SET,67
+ok
</b></br><br>
or this - note the extra Daily value</br> 
<b>
AT+SENDICA=property,PowerSwitch,1,Daily,0.10,Plant,0.16,Emission,0.09,Time,30,P_adj,66,TEMP_SET,67
+ok</br></br>
</b>
<p>For some reason, which I haven't got my head round, sometimes it includes the Daily energy before the Plant (Trees) in the second send - it might only send it when this is greater than 0.01 but its a strange one i've written round to be sure i don't throw an error and only upload the daily if its there</p>

Initialy I tapped the HF-LPT270 UART by tracing the output pins to the JP4 header on the inverter main board and inserted jumper cables to an open logger and collected the data to a text file on a sdcard to see what I have.</br></br>

![Capture3](https://user-images.githubusercontent.com/18092613/234678467-3cc8e391-3103-483f-9b58-dfbc72d7a9f2.JPG)


The first versions of the python script read this data from a copy of the text file and then formats the data to be processesed before uploading to ThinkSpeak.
![Inked20230415_133328_LI](https://user-images.githubusercontent.com/18092613/234235022-c4843dd2-7ab7-402a-93a3-801890a17e90.jpg)

I added a 2 min delay as this simulated how often i would normally send to make sure the free thinkspeak update limits are met

<b>Implementing The Pi</b>

![20230430_163231](https://user-images.githubusercontent.com/18092613/235365455-16fb6488-a7b9-40fe-8787-7cbd85594602.jpg)

![PIPINS](https://user-images.githubusercontent.com/18092613/234257432-985cef0f-196d-4d22-b502-a0df802867ba.JPG)

Using a Pi Zero (Wifi edition) (about £15) I've taken the tap for the open logger and transfered the + to the 5v in (Pin 4), Ground to  the Pi Ground (Pin 6) and UART TX to the Pi's UART RX (GPIO 15 pin 10).  Even though it's only 3.3 volts coming from the UART of the inverter this is enough to power the PiZero and handle the load.  <br><br>
I've not connected anything from the TX pin of the PI back to the HF-LPT270 UART as i've no need to write back at this point and am only interested in collecting data for analysis


<b>To Use</b><br>
Register with a free ThingSpeak account - a free account is enough requests for between 2 and 4 minutes upload schedule.  I'll be setting mine to 5 minutes

![image](https://user-images.githubusercontent.com/18092613/233067232-51e05831-b3dd-4651-9f8d-82283e4708a2.png)
  
Make a note of your API key.  You will need to set this in your copy of the python script

Set up your fields to match the image below
  
![Capture](https://user-images.githubusercontent.com/18092613/234677141-04bc95c9-53bc-4499-9972-5cbd558222a9.JPG)


Congigure your graphs - see my example.  THis is up to you really.  

![Capture](https://user-images.githubusercontent.com/18092613/236232260-4ddc080b-ae5f-4b26-9f4a-7cf8dd2fd8ca.JPG)


 <BR><BR>
 For autostarting i'm using the following in my CRONTAB (crontab -e to edit)  <b>@reboot nohup python solar/solar_rx.py &</b>
 <BR><BR>
   
 I've currently set my upload time to 30 seconds - This is using about 1200 messages a day - the free account allows for 8219 messages a day.  No doubt i'll use more in the longer days but i don't expect to go over the free limit.
   
 ![Capture](https://user-images.githubusercontent.com/18092613/236614792-a8ae8a8a-ab53-4a42-bed2-ead31fe40d53.JPG)

 You can view my public channel to see the data being generated by 2 x 230w Craig Solar Panels on my shed roof and a WVC700 Grid tie invter<BR>
   <p>www.craigsolar.co.uk</p>
 https://thingspeak.com/channels/2110110

