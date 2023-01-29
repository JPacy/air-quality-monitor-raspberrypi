#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cosens.py
#  
#  Copyright 2023  <jpq@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import influxdb_client, os, time
import RPi.GPIO as GPIO
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from senseair_s8 import SenseairS8

# Set pin mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
# Define pins
greenLed = 17
yellowLed = 27
redLed = 22

# Setup database
token = os.environ.get("INFLUXDB_TOKEN")
org = "Embedded Systems and Computer Engineering"
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="CO2 sensor"

write_api = client.write_api(write_options=SYNCHRONOUS)

# Create instance of senseairS8 object
senseair_s8 = SenseairS8()

while True:
    print(senseair_s8.co2())
    
    # Display indicator LED
    if (senseair_s8.co2() <= 1000):
        GPIO.output(greenLed, True)
        GPIO.output(yellowLed, False)
        GPIO.output(redLed, False)
    elif (senseair_s8.co2() < 2000 and senseair_s8.co2() > 1000):
        GPIO.output(greenLed, False)
        GPIO.output(yellowLed, True)
        GPIO.output(redLed, False)
    else:
        GPIO.output(greenLed, False)
        GPIO.output(yellowLed, False)
        GPIO.outpur(redLed, True)
        
    # Setup data to send
    point = (
        Point("measurement")
        .tag("CO2", "Level")
        .field("PPM", senseair_s8.co2())
    )
    write_api.write(bucket=bucket, org="Embedded Systems and Computer engineering", record=point)
    time.sleep(5)


