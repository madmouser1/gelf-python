class Message():
	version = "1.0"
	shortMessage = ""
	fullMessage = ""
	level = 0
	host = ""
	gfile = ""
	line = 1
	timestamp = ""
	facility = 1

class Client():
	graylog2_server = "127.0.0.1"
	graylog2_port = 12201
	lanMaxChunkSize = 1420
	wanMaxChunkSize = 8154
