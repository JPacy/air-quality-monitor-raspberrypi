# air-quality-monitor-raspberrypi

This project interfaces a Senseair S8 (CO2-sensor) and a Nova SDS011 (PM2.5/10 sensor) with an raspberry pi 4 model B. 
The sensor readout is done using a python script for both the Senseair S8 and Nova SDS011. This python script also sends the data
from the sensors to an InfluxDB database using their API. Then the data gets visualized using Grafana, an open-source analytics and interactive visualization web-application.

## IoT pipeline 
![alt text](https://github.com/JPacy/air-quality-monitor-raspberrypi/blob/main/IoTPipeline.jpeg)

## Resources
- https://gist.github.com/geoffwatts/b0b488b5a5257223ed53 (Sensor readout Nova SDS011)
- https://pypi.org/project/senseair-s8/ (Sensor readout Senseair S8)
- https://cdn-reichelt.de/documents/datenblatt/X200/SDS011-DATASHEET.pdf (Nova SDS011 Datasheet)
-https://www.youtube.com/watch?v=Cmr5VNALRAg&t=681s&ab_channel=JeffGeerling (Inspiration for this project)
