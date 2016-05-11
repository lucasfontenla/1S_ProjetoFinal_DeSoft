import time, socket
  
#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte 

class Client():
	def __init__(self):
		self.port = 5000

	def serverHost(self, serverIP):
		self.hostServer = serverIP

	def clientStart(self):
		self.connection_status = 'none'
		self.c = socket.socket()
		self.c.connect((self.hostServer, self.port))

		self.c.setblocking(0)
		timeout0 = time.clock()

		data = str()

		self.checkStatus('trying to connect')

		while True:
				if time.clock()-timeout0 >= 20:
					timeout = True
					break
				else:
					timeout = False
					try:
						data = self.c.recv(1024)
						if data:
							if data == 'connected as principal'.encode():
								self.checkStatus('Connected as principal')
								break
							elif data == 'connected'.encode():
								self.checkStatus('Connected')
								break
					except:
						pass

		if timeout:
			self.checkStatus('Error 001 Timeout: could not connect to server in time')
		else:
			if self.connection_status == 'Connected as principal':
				return 'done: principal'
			else:
				return 'done: not principal'
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def closeConnection(self):
		self.c.send('close'.encode())
#----------------------------------------------------------------------------------------------------------------------------------------------------------------		
	def getMyTeam(self):	
		self.myteam = 'none'
		self.c.setblocking(1)
		data = self.c.recv(1024)
		self.myteam = str(data)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def checkStatus(self, value):
		self.connection_status = value
		print(value)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def myTeam(self):
		return self.myteam
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def StartGame(self):
		self.c.send('start game'.encode())
		self.waitStart()

	def waitStart(self):
		while True:
			data = self.c.recv(1024)
			if data == 'start'.encode():
				break
			else:
				pass
		print('started')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def sendPackages(self, value):
		print(value)
		self.c.send(str(value).encode())

	def endServer(self):
		self.c.send('end server'.encode())
		self.c.close()		

client = Client()
client.serverHost('127.0.0.1')
value = client.clientStart()
if value == 'done: principal':
	time.sleep(10)
	client.closeConnection()
	print(client.connection_status)
	client.getMyTeam()
	print(client.myTeam())
	client.StartGame()
	for i in range(0, 100):
		client.sendPackages(500)
		time.sleep(.5)
	client.endServer()
else:
	print(client.connection_status)
	client.getMyTeam()
	print(client.myTeam())
	client.waitStart()
	for i in range(0, 100):
		client.sendPackages(500)
		time.sleep(.5)