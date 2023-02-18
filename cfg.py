import socket

mqttserver_ip="192.168.15.65"
mqttserver_port=1883

hostname = socket.gethostname()
server_ip  = socket.gethostbyname(hostname)
server_port=5000

print(f"Hostname: {hostname}, IP Address: {server_ip}:{server_port}")