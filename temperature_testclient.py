import paho.mqtt.client as mqtt

# Define the MQTT broker address and port
broker_address = "192.168.15.65"
broker_port = 1883

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")

# Create a new MQTT client instance
client = mqtt.Client()

# Set the callback function for when a message is received
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the topic
client.subscribe("dashboard/dummy/#")

# Start the MQTT client loop
client.loop_forever()
