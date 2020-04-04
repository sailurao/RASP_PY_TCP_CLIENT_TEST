#https://www.techbeamers.com/python-tutorial-write-tcp-server/
import socket
from gpiozero import LED
led = LED(17)
host_ip, server_port = "10.7.1.133", 8081
data = "OM SRI RAM"

# Initialize a TCP client socket using SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	# Establish connection to TCP server and exchange data
        tcp_client.connect((host_ip, server_port))
	count = 0
	while count == 0:
		tcp_client.sendall(data.encode())
                led.on()
		# Read data from the TCP server and close the connection
		received = tcp_client.recv(1024)
		led.off()
		#print ("Bytes Received: {}".format(received.decode()))
finally:
        #tcp_client.close()
        print ("***")



