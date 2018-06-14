import socket
#from ServerApps import *

class ClientApp(object):
	""" 
	A python object dealing with client applications \n
	in client-server network programming and simulation.
	"""

	def simulateData(self, clientSocket):
		""" A function to establish connection with the server \n
		and facilitate communication.
		"""
		return clientSocket.sendall(b'Hello,world!')

	def recvMessage(self,clientSocket):

		return clientSocket.recv(1024)

	def startClient(self):
		""" 
		A python function to create and initiate client communication \n
		within a client-server network programming and simulation for client apps.
		
		+++++++++++++++++++++++++++++++++
		General Concepts are:
		1. Create a SOCKET.
		2. BIND* to a server.
		3. CONNECT to a server.
		4. SEND?RECV - repeat until we have or receive data
		5. SHUTDOWN to end read/write
		6. CLOSE to release data
		+++++++++++++++++++++++++++++++++++

		"""

		#Create a socket object
		clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		#Get local machine name
		host = socket.gethostname()

		port = 9999

		# make Connection to hostname on the port
		clientSocket.connect((host, port))

		#Simulate and send data
		dt = self.simulateData(clientSocket)

		tm = self.recvMessage(clientSocket)
		#tm = clientSocket.recv(1024)

		clientSocket.close()

		#print(" The time got from the server is %s " % tm.decode('ascii'))
		print('Received: ', repr(tm))

	def run(self):
		self.startClient()

if __name__ == '__main__':
	obj = ClientApp()
	obj.run()