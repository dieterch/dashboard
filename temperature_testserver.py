import paho.mqtt.client as mqtt
import datetime, time

# Set up the MQTT client and connect to the local Mosquitto broker
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)

# Set up a loop to send sample data every 10 seconds
while True:
    # Generate a sample temperature reading
    temperature = round(25 + (time.time() % 5), 2)

    # Publish the temperature reading to the MQTT topic
    mqtt_client.publish('test_temperature', temperature)

    print(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}\t{temperature:.2f}")
    # Wait for 10 seconds before sending the next reading
    time.sleep(10)
