import sys
# sys.path.append('/ClientApps/')
# sys.path.append('/ServerApps/')

# from ServerApps.ServerApp 
from ServerApps.ServerApp import ServerApp as sa
# from ClientApps.ClientApp import ClientApp

# def simulateData(self, clientSocket):
# 	""" A function to establish connection with the server \n
# 	and facilitate communication.
# 	"""
# 	return clientSocket.sendall(b'Hello,world!')
	
# ServerApp()
# ClientApp()
print(sa.getTime())