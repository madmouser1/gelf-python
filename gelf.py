from socket import *
import zlib

class Client():

	def __init__(self, server='localhost', port=12201, maxChunkSize=8154):
		self.graylog2_server = server
		self.graylog2_port = port
		self.maxChunkSize = maxChunkSize

	def log(self, message):
		UDPSock = socket(AF_INET,SOCK_DGRAM)
		zmessage = zlib.compress(message)
		UDPSock.sendto(zmessage,(self.graylog2_server,self.graylog2_port))
		UDPSock.close()
