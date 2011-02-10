class GELFMessage:
	VERSION = "1.0"
	graylog_server = "127.0.0.1"
	graylog_port = 12201 
	maxChunkSize = "WAN"
	data =

	def construct(graylog_server, graylog_port, maxChunkSize = "WAN"):
		
