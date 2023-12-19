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
token = "aMqlANBnsxVntGrmYdXMQLfJL2NicBTuTswQ12dqtQBdqgvAqFA2udJsjE0_o8IzFCSVi3ZHJIWXTXWIEeomNQ=="
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
    client.subscribe("Sensor DS1")
    client.subscribe("Sensor DPIR1")
    client.subscribe("Sensor RPIR1")
    client.subscribe("Sensor RPIR2")
    client.subscribe("Keypads")
    client.subscribe("Distance")


mqtt_client.on_connect = on_connect
mqtt_client.on_message = lambda client, userdata, msg: save_to_db(json.loads(msg.payload.decode('utf-8')))


def save_to_db(data):
    write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
    timestamp = datetime.fromisoformat(data["timestamp"]) if "timestamp" in data else datetime.utcnow()
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

# Route to store dummy data
# @app.route('/store_data', methods=['POST'])
# def store_data():
#     try:
#         data = request.get_json()
#         store_data(data)
#         return jsonify({"status": "success"})
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)})
#
#
# def handle_influx_query(query):
#     try:
#         query_api = influxdb_client.query_api()
#         tables = query_api.query(query, org=org)
#
#         container = []
#         for table in tables:
#             for record in table.records:
#                 container.append(record.values)
#
#         return jsonify({"status": "success", "data": container})
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)})
#
#
# @app.route('/simple_query', methods=['GET'])
# def retrieve_simple_data():
#     query = f"""from(bucket: "{bucket}")
#     |> range(start: -10m)
#     |> filter(fn: (r) => r._measurement == "Humidity")"""
#     return handle_influx_query(query)
#
#
# @app.route('/aggregate_query', methods=['GET'])
# def retrieve_aggregate_data():
#     query = f"""from(bucket: "{bucket}")
#     |> range(start: -10m)
#     |> filter(fn: (r) => r._measurement == "Humidity")
#     |> mean()"""
#     return handle_influx_query(query)


if __name__ == '__main__':
    app.run(debug=True)
