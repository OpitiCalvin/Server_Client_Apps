import socket

class ServerApp:
	""" A python object for server creation.
	"""

	def __init__(self, host=socket.gethostname(),port=9999):
		#get local machine name
		self.host = host
		#Define/initialize port
		self.port = port
	

	def getHostName(self):
		return str(self.host) + ":" + str(self.port)

	def createServer(self):
		"""Create a server application.

		++++++++++++++++++++++++++++++

		General Concepts:
		1. Create a SOCKET - Get the file descriptor!
		2. BIND to an address - What port am I on?
		3. LISTEN on a port, and wait for a connection to be established.
		4. ACCEPT the connection from a client.
		5. SEND/RECV - the same way we read and write for a file.
		6. SHUTDOWN - to end read/write.
		7. CLOSE  - to release data.
		++++++++++++++++++++++++++++++++++
		"""
		#create a socket object
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		#get local machine name
		#host = socket.gethostname()

		#Define/initialize port
		#self.port = 9999

		#Bind to the port
		serverSocket.bind((self.host, self.port))

		#Queue up for 5 requests
		serverSocket.listen(5)
		print("Server Listening on %s:%s and waiting for connection..."% (self.host, self.port))

		#return serverSocket
		self.sendMessage(serverSocket)
		

	def getTime():
		""" A function to determine and communicate current server time.
		"""
		import time

		return time.ctime(time.time()) + "\n"
		
	def sendMessage(self, servSocket):
		"""
		A function that connects to a client application.
		"""
		#servSocket = self.createServer()
		while True:
			clientSocket, addr = servSocket.accept()

			print("Got a connection from %s " % str(addr))
			
			#communicate current time
			# currentTime = self.getTime()
			# clientSocket.send(currentTime.encode('ascii'))
			
			data = clientSocket.recv(1024)
			if not data: break
			clientSocket.sendall(data)
			
			#Close connection
		clientSocket.close()

	def run(self):
		self.createServer()


if __name__ == '__main__':
	obj = ServerApp()
	obj.run()