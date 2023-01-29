#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pmsens.py
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

from __future__ import print_function
from serial import Serial, EIGHTBITS, STOPBITS_ONE, PARITY_NONE
import time, struct
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
# Create database
token = os.environ.get("INFLUXDB_TOKEN")
org = "Embedded Systems and Computer Engineering"
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="PM sensor"

write_api = client.write_api(write_options=SYNCHRONOUS)

# Initialize port
port = "/dev/ttyUSB0" # Serial port
baudrate = 9600

# Prepare serial connection.
ser = Serial(port, baudrate=baudrate, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE)
ser.flushInput()

HEADER_BYTE = b"\xAA"
COMMANDER_BYTE = b"\xC0"
TAIL_BYTE = b"\xAB"

byte, previousbyte = b"\x00", b"\x00"

while True:
    previousbyte = byte
    byte = ser.read(size=1)
    print(byte)
    
    if previousbyte == HEADER_BYTE and byte == COMMANDER_BYTE:
        packet = ser.read(size=8)
        print(packet)
        
        readings = struct.unpack('<HHcccc', packet)
        
        # Measurements
        pm_25 = readings[0] / 10.0
        pm_10 = readings[1] / 10.0
        
        #Sensor ID
        id = packet[4:6]
        print(id)
        
        # Prepare checksums
        checksum = readings[4][0]
        calculated_checksum = sum(packet[:6]) & 0xFF
        checksum_verified = (calculated_checksum == checksum)
        print(checksum_verified)
        
        # Message tail
        tail = readings[5]
        
        if tail == TAIL_BYTE and checksum_verified:
            print("PM 2.5:", pm_25, "ug/m^3 PM 10:", pm_10, "ug/m^3")
            
            # setup data to send
            point = (
                Point("measurement")
                .tag("PM25", "Level")
                .field("PM25", pm_25)
            )
            
            write_api.write(bucket=bucket, org="Embedded Systems and Computer engineering", record=point)
            
            point = (
                Point("measurement")
                .tag("PM10", "Level")
                .field("PM10", pm_10)
            )
            
            write_api.write(bucket=bucket, org="Embedded Systems and Computer engineering", record=point)
            time.sleep(5)
