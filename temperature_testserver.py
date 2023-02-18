import paho.mqtt.client as mqtt
import datetime, time

# Set up the MQTT client and connect to the local Mosquitto broker
mqtt_client = mqtt.Client()
mqtt_client.connect("192.168.15.65", 1883, 60)

# Set up a loop to send sample data every 10 seconds
while True:
    # Generate a sample temperature reading
    temperature = round(25 + (time.time() % 5), 2)
    humidity = round(40 - (time.time() % 5), 2)
    baro_pressure = round((97 + (time.time() % 5))/100.0, 2)

    # Publish the temperature and humidity reading to the MQTT topic
    mqtt_client.publish('dashboard/dummy/temperature', temperature)
    mqtt_client.publish('dashboard/dummy/humidity', humidity)
    mqtt_client.publish('dashboard/dummy/baro_pressure', baro_pressure)

    print(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}\tTemp: {temperature:.2f}\tHumid: {humidity:.2f}\tBaro:{baro_pressure:.2f}")
    # Wait for 10 seconds before sending the next reading
    time.sleep(10)
