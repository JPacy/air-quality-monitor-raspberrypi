# air-quality-monitor-raspberrypi

## Introduction
Bad air can be hazardous to our health, that is why I decided to make a air quality monitor. This will enable me to monitor the levels of CO2, PM2.5 and PM10 in my room. Once the air quality reaches an unhealthy threshold I will be able to see it and take action, for instance open an window. 
This project interfaces a Senseair S8 (CO2-sensor) and a Nova SDS011 (PM2.5/10 sensor) with an raspberry pi 4 model B. 
The sensor readout is done using a python script for both the Senseair S8 and Nova SDS011. This python script also sends the data
from the sensors to an InfluxDB database using their API. Then the data gets visualized using Grafana, an open-source analytics and interactive visualization web-application.


## IoT pipeline 
![alt text](https://github.com/JPacy/air-quality-monitor-raspberrypi/blob/main/IoTPipeline.jpeg)

## How it works

### Sensor readout
The sensor readout is done using 2 python scripts. One for the Nova SDS011 (pmsens.py) and the other script for the Senseair S8 (cosens.py). Both the scripts also use the InfluxDB API to send data to an InfluxDB database. 

### Database 
InfluxDB is an open-source time-series database. This database is used to store our sensor data. 

### Grafana
The data that is stored in our database gets queried using Grafana, which is an open-source analytics and interactive visualization web-application.

## Resources
- https://gist.github.com/geoffwatts/b0b488b5a5257223ed53 (Sensor readout Nova SDS011)
- https://pypi.org/project/senseair-s8/ (Sensor readout Senseair S8)
- https://cdn-reichelt.de/documents/datenblatt/X200/SDS011-DATASHEET.pdf (Nova SDS011 Datasheet)
- https://www.youtube.com/watch?v=Cmr5VNALRAg&t=681s&ab_channel=JeffGeerling (Inspiration for this project)
