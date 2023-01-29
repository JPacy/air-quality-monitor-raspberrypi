# air-quality-monitor-raspberrypi

## Introduction
Bad air can be hazardous to our health, that is why I decided to make a air quality monitor. This will enable me to monitor the levels of CO2, PM2.5 and PM10 in my room. Once the air quality reaches an unhealthy threshold I will be able to see it and take action, for instance open an window. 
This project interfaces a Senseair S8 (CO2-sensor) and a Nova SDS011 (PM2.5/10 sensor) with an raspberry pi 4 model B. 
The sensor readout is done using a python script for both the Senseair S8 and Nova SDS011. This python script also sends the data
from the sensors to an InfluxDB database using their API. Then the data gets visualised using Grafana, an open-source analytics and interactive visualization web-application.


## IoT pipeline 
![alt text](https://github.com/JPacy/air-quality-monitor-raspberrypi/blob/main/IoTPipeline.jpeg)

## How it works

### Sensor readout
The sensor readout is done using 2 python scripts. One for the Nova SDS011 (pmsens.py) and the other script for the Senseair S8 (cosens.py). Both the scripts also use the InfluxDB API to send data to an InfluxDB database. 

### Database 
InfluxDB is an open-source time-series database. This database is used to store our sensor data. 

### Grafana
The data that is stored in our database gets queried using Grafana, which is an open-source analytics and interactive visualization web-application. This makes visualisation of the data possible in a graph. 

### LED indicator
The prototype also has 3 LED indicators. These LED's will light up depending on the CO2 level in the air. The LED will be green if the air 
has a CO2 concentration less than 1000 ppm, yellow if the CO2 concentration is less than 2000 but above 1000 and finally red if the CO2 concentration is above 2000 ppm.

![](https://github.com/JPacy/air-quality-monitor-raspberrypi/blob/main/air-monitor-grafana-dashboard.png)

### Prototype
![](https://github.com/JPacy/air-quality-monitor-raspberrypi/blob/main/air-monitor-prototype.jpg)

#### Connections
![](https://github.com/JPacy/air-quality-monitor-raspberrypi/blob/main/senseair_connection.png) (image from http://co2meters.com/Documentation/AppNotes/AN168-S8-raspberry-pi-uart.pdf)

The Nova SDS011 can be connected directly to an USB-port, as it comes with a USB-to-Serial converter. (See image in Prototype section)

#### Demo
https://youtu.be/424DJOA0QDk

## Process
This project started with only having a raspberry pi 4. Then I got the idea to make an air quality monitor. I thought about which metrics
would be important for air quality and come to the conclusion that PM2.5 and PM10 are important metrics. So then I searched for a PM-sensor. 
I eventually found the Nova SDS011. I chose this sensor because it is easy to interface with an raspberry pi. 

Then I also found out that in an indoor environment, the CO2 level also contributes a lot to our well-being. That is why I also chose to
monitor the CO2 level. I did this by adding a Senseair S8 sensor to the raspberry pi. 

After the sensors were coneected to the raspberry pi, I wrote two separate python scripts, one for each sensor. These scripts send the sensor data
to an InfluxDB database. I chose for InfluxDB, because it is open-source and suitable for time-series data. Besides it is also supported in Grafana.
This makes it easy to query and visualise the data on a dashboard in Grafana.

## Credits
The inspiration for this project came from a youtube video mentioned in the resources section.

## Resources
- https://gist.github.com/geoffwatts/b0b488b5a5257223ed53 (Sensor readout Nova SDS011)
- https://pypi.org/project/senseair-s8/ (Sensor readout Senseair S8)
- https://cdn-reichelt.de/documents/datenblatt/X200/SDS011-DATASHEET.pdf (Nova SDS011 Datasheet)
- https://www.youtube.com/watch?v=Cmr5VNALRAg&t=681s&ab_channel=JeffGeerling (Inspiration for this project)
- http://co2meters.com/Documentation/AppNotes/AN168-S8-raspberry-pi-uart.pdf (Connections for Senseair S8)
