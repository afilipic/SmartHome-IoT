from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import paho.mqtt.client as mqtt
import json
from dotenv import load_dotenv
import os
from datetime import datetime

class Home(object):
    def __init__(self,pin):
        self.people_count = 0
        self.alarm = False
        self.alarm_pin = pin
        self.token = "GpQ8pcMQcfkWTR-O6xY7qFgBfoBNOKZNxkHMU1l4DLpyiFoKoDznZiuIUjoOtA-2pgCszUh-aX7i0JOCBR4dig=="
        self.org = "FTN"
        self.url = "http://localhost:8086"
        self.bucket = "example_db"
        self.influxdb_client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        self.is_security_on = True

    def more_people(self):
        self.people_count += 1

    def less_people(self):
        if (self.people_count > 0):
            self.people_count -= 1

    def set_alarm_true(self):
        if self.is_security_on == False:
            return
        self.alarm = True
        write_api = self.influxdb_client.write_api(write_options=SYNCHRONOUS)
        timestamp = datetime.utcnow()
        point = (
            Point("Alarm")
                .tag("simulated", True)
                .tag("name", "House Alarm")
                .field("measurement", True)
                .time(timestamp)
        )
        write_api.write(bucket=self.bucket, org=self.org, record=point)

    def set_security_on(self):
        self.is_security_on = True

    def set_alarm_false(self):
        self.alarm = False
        self.is_security_on = False
        write_api = self.influxdb_client.write_api(write_options=SYNCHRONOUS)
        timestamp = datetime.utcnow()
        point = (
            Point("Alarm")
                .tag("simulated", True)
                .tag("name", "House Alarm")
                .field("measurement", False)
                .time(timestamp)
        )
        write_api.write(bucket=self.bucket, org=self.org, record=point)
