import time, socket
  
#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte 

class Client():
	def __init__(self):
		self.port = 80

	def serverHost(self, serverIP):
		self.hostServer = serverIP
		self.serveraddr = (self.hostServer, self.port)

	def setName(self, strName):
		self.clientName = strName
		print('My Name: ', strName)

	def clientStart(self):
		self.connection_status = 'none'
		self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		self.client.setblocking(1)
		timeout0 = time.clock()

		data = str()

		self.checkStatus('trying to connect')

		while True:
				if time.clock()-timeout0 >= 20:
					timeout = True
					break
				else:
					timeout = False
					first_send = self.clientName+':hello server'
					self.client.sendto((first_send.encode()), self.serveraddr)
					data, addr = self.client.recvfrom(1024)
					if data:
						if addr[0] == self.hostServer:
							if data == 'connected as principal'.encode():
								self.checkStatus('Connected as principal')
								break
							elif data == 'connected'.encode():
								self.checkStatus('Connected')
								break

		print('Time elapsed:', round(time.clock()-timeout0, 3), 's')
		if timeout:
			self.checkStatus('Error 001 Timeout: could not connect to server in time')
		else:
			if self.connection_status == 'Connected as principal':
				return 'done: principal'
			else:
				return 'done: not principal'
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def closeConnection(self):
		self.client.sendto(':close'.encode(), self.serveraddr)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------		
	def getMyTeam(self):	
		self.myteam = 'none'
		self.client.setblocking(1)
		while True:
			data, addr = self.client.recvfrom(1024)
			if addr[0] == self.hostServer:
				self.myteam = str(data)
				break	
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def checkStatus(self, value):
		self.connection_status = value
		print(value)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def myTeam(self):
		return self.myteam
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def StartGame(self):
		self.client.sendto('start game'.encode(), self.serveraddr)
		self.waitStart()

	def waitStart(self):
		while True:
			data, addr = self.client.recvfrom(1024)
			if addr[0] == self.hostServer:
				if data == 'start'.encode(): break
		print('started')
		
	def sendPackages(self, value):
		self.client.sendto(str(value).encode(), self.serveraddr)
		return 'sent'

	def recivePoints(self):
		while True:
			data, addr = self.client.recvfrom(1024)
			if addr[0] == self.hostServer: break
		return str(data)


	def stopReceiving(self):
		self.client.sendto('stop receiving'.encode(), self.serveraddr)
		self.client.close()	

	def dataTreatment(self, value):
		pass