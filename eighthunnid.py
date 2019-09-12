import socket

def udpsend(message):
    UDP_IP = "172.20.10.5"
    UDP_PORT = 5005
    MESSAGE = str(message)


    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))