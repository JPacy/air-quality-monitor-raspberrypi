# air-quality-monitor-raspberrypi

This project interfaces a Senseair S8 (CO2-sensor) and a Nova SDS011 (PM2.5/10 sensor) with an raspberry pi 4 model B. 
The sensor readout is done using a python script for both the Senseair S8 and Nova SDS011. This python script also sends the data
from the sensors to an InfluxDB database using their API. Then the data gets visualized using Grafana, an open-source analytics and interactive visualization web-application.

## IoT pipeline 
![alt text](https://github.com/JPacy/air-quality-monitor-raspberrypi/blob/main/IoTPipeline.jpeg | width = 200)
