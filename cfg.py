import socket
import fcntl
import struct

# see:
# https://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-from-a-nic-network-interface-controller-in-python
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

mqttserver_ip="192.168.15.65"
mqttserver_port=1883

hostname = socket.gethostname()
#server_ip  = socket.gethostbyname(hostname)
server_ip  = get_ip_address()
server_port=5000

# def get_ip_address2(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(
#         s.fileno(),
#         0x8915,  # SIOCGIFADDR
#         struct.pack('256s', ifname[:15])
#     )[20:24])

print(f"Hostname: {hostname}, IP Address: {server_ip}:{server_port}")
#print(f"get_ip_address: {get_ip_address()}")
#print(f"get_ip_address2('eth0'): {get_ip_address2(b'eth0')}")
