from flask import Flask, jsonify, request
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import paho.mqtt.client as mqtt
import json
from dotenv import load_dotenv
import os
from datetime import datetime
from flask_socketio import SocketIO
from flask_cors import CORS

load_dotenv()


app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


# InfluxDB Configuration
token = "GpQ8pcMQcfkWTR-O6xY7qFgBfoBNOKZNxkHMU1l4DLpyiFoKoDznZiuIUjoOtA-2pgCszUh-aX7i0JOCBR4dig=="
org = "FTN"
url = "http://localhost:8086"
bucket = "example_db"
influxdb_client = InfluxDBClient(url=url, token=token, org=org)


# MQTT Configuration
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_start()


def send_alarm_message_ws(topic, message):
    try:
        socketio.emit(topic, message)
    except Exception as e:
        print(e)

def on_connect(client, userdata, flags, rc):
    client.subscribe("Temperature")
    client.subscribe("Humidity")
    client.subscribe("Door Sensor")
    client.subscribe("Sensor")
    client.subscribe("Keypads")
    client.subscribe("BIR")
    client.subscribe("Time")
    client.subscribe("BRGB")
    client.subscribe("Distance")
    client.subscribe("Door Buzzer")
    client.subscribe("Led Diode")
    client.subscribe("Gyroscope")
    client.subscribe("GYRO")
    client.subscribe("LCD")
    client.subscribe("Number of people")


alarm_counter = True

mqtt_client.on_connect = on_connect



mqtt_client.on_message = lambda client, userdata, msg: save_to_db(json.loads(msg.payload.decode('utf-8')))

def save_to_db(data):
    global alarm_counter
    write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
    timestamp = datetime.fromisoformat(data["timestamp"]) if "timestamp" in data else datetime.utcnow()
    #print(data)
    if 'alarm' in data and data['alarm'] and alarm_counter:
        try:
            socketio.emit("alarm", "aktiviraj")
        except Exception as e:
            print(e)
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
        .time(timestamp)
    )
    #print(point)
    write_api.write(bucket=bucket, org=org, record=point)


@app.route('/')
def home():
    return f"Secret Key: {token}"

@app.route('/activate_alarm', methods=['PUT'])
def activate_alarm():
    global alarm_counter
    try:
        print("ALARM SE PALI")
        try:
            alarm_counter = True
            mqtt_client.publish("activate_alarm", "")
        except Exception as e:
            print(e)
        return jsonify({"response": "ALARM JE UPALJEN"})
    except Exception as e:
        return jsonify({"response": "GRESKA - " + str(e)})

@app.route('/deactivate_alarm',methods= ["PUT"])
def deactivate_alarm():
    global alarm_counter
    try:
        print("ALARM SE GASI")
        try:
            alarm_counter = False
            mqtt_client.publish("deactivate_alarm", "")
        except Exception as e:
            print(e)
        return jsonify({"response": "ALARM JE UGASEN"})
    except Exception as e:
        return jsonify({"response": "GRESKA - " + str(e)})

@app.route("/schedule_alarm/<string:time>", methods=["put"])
def schedule_alarm(time):
    try:
        print(time, "postavi alarm u ovoliko sati")
        # format string-a: 2024-01-10T23:38
        try:
            mqtt_client.publish("schedule_alarm", time)
            print(time)
        except Exception as e:
            print(e)
        # pin treba proslediti preko mqtt simulatoru
        return jsonify({"response": "ALARM JE POSTAVLJEN  " + time})
    except Exception as e:
        return jsonify({"response": "GRESKA - " + str(e)})



if __name__ == '__main__':
    app.run(debug=True, port=8085)

