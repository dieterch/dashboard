from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO, emit
import paho.mqtt.client as mqtt
from flask_cors import CORS
import cfg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app, origins=['http://192.168.15.23:5000'])
CORS(app, origins=[f"http://{cfg.server_ip}:{cfg.server_port}"])

# Set up the MQTT client and connect to the local Mosquitto broker
mqtt_client = mqtt.Client()
mqtt_client.connect(cfg.mqttserver_ip, cfg.mqttserver_port, 60)

# Set up a callback function to handle incoming MQTT messages
def on_message(client, userdata, message):
    # Forward the MQTT message to the WebSocket client
    # print("message received " ,str(message.payload.decode("utf-8")))
    socketio.emit('mqtt_message', {'topic': message.topic, 'payload': message.payload.decode()})

# Set up the Flask route to serve the Vue HTML
@app.route('/')
def index():
    #server_ip = request.host.split(':')[0]
    #server_port = request.host.split(':')[1]
    data = {
        'server_ip': cfg.server_ip,
        'server_port': cfg.server_port
    }
    return render_template('index.html', data= { 'server_ip': cfg.server_ip, 'server_port': cfg.server_port})

# Set up the WebSocket connection
@socketio.on('connect')
def handle_connect():
    print('WebSocket client connected')
    # Subscribe to the MQTT topic when the WebSocket client connects
    mqtt_client.subscribe('dashboard/dummy/#')

# Set up the WebSocket disconnection
@socketio.on('disconnect')
def handle_disconnect():
    print('WebSocket client disconnected')

if __name__ == '__main__':
    # Set up the MQTT client to handle incoming messages
    handle_connect()
    mqtt_client.on_message = on_message
    mqtt_client.loop_start()
    socketio.run(app, host=cfg.server_ip, port=cfg.server_port, debug=True)
