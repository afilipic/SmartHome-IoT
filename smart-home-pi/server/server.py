from flask import Flask, jsonify, request
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import paho.mqtt.client as mqtt
import json
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()


app = Flask(__name__)


# InfluxDB Configuration
token = "M1A2wRiRjKnYkHaz7VnmLT653YT-cZVqv0Br0HbhEzcYM7wP1Hvd5PcfmUpLaAZG_EGsWrhjRfueUcFAO8Qbow=="
org = "FTN"
url = "http://localhost:8086"
bucket = "example_db"
influxdb_client = InfluxDBClient(url=url, token=token, org=org)


# MQTT Configuration
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_start()


def on_connect(client, userdata, flags, rc):
    client.subscribe("Temperature")
    client.subscribe("Humidity")
    client.subscribe("Door Sensor")
    client.subscribe("Sensor")
    client.subscribe("Keypads")
    client.subscribe("Time")
    client.subscribe("BIR")
    client.subscribe("BRGB")
    client.subscribe("Distance")
    client.subscribe("Door Buzzer")
    client.subscribe("Led Diode")
    client.subscribe("Gyroscope")
    client.subscribe("GYRO")
    client.subscribe("LCD")

mqtt_client.on_connect = on_connect
mqtt_client.on_message = lambda client, userdata, msg: save_to_db(json.loads(msg.payload.decode('utf-8')))

def save_to_db(data):
    write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
    timestamp = datetime.fromisoformat(data["timestamp"]) if "timestamp" in data else datetime.utcnow()
    print(data)
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
        .time(timestamp)
    )
    print(point)
    write_api.write(bucket=bucket, org=org, record=point)


@app.route('/')
def home():
    return f"Secret Key: {token}"



if __name__ == '__main__':
    app.run(debug=True, port=8085)

