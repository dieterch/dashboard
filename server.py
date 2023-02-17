from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, emit
import paho.mqtt.client as mqtt
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
CORS(app, origins=['http://192.168.15.65:5000', 'http://127.0.0.1:5000'])

# Set up the MQTT client and connect to the local Mosquitto broker
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)

# Set up a callback function to handle incoming MQTT messages
def on_message(client, userdata, message):
    # Forward the MQTT message to the WebSocket client
    #print("message received " ,str(message.payload.decode("utf-8")))
    socketio.emit('mqtt_message', {'topic': message.topic, 'payload': message.payload.decode()})

# Set up the Flask route to serve the Vue HTML
@app.route('/')
def index():
    return render_template('index.html')

# Set up the WebSocket connection
@socketio.on('connect')
def handle_connect():
    print('WebSocket client connected')
    # Subscribe to the MQTT topic when the WebSocket client connects
    mqtt_client.subscribe('test_temperature')

# Set up the WebSocket disconnection
@socketio.on('disconnect')
def handle_disconnect():
    print('WebSocket client disconnected')

if __name__ == '__main__':
    # Set up the MQTT client to handle incoming messages
    handle_connect()
    mqtt_client.on_message = on_message
    mqtt_client.loop_start()
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
