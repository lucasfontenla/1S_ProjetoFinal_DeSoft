import time, socket
from threading import Thread  

#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte 

class Client():
	def __init__(self):
		self.port = 80

	def showMyHost(self):
		return [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][1]

	def setHost(self, serverIP):
		self.hostServer = serverIP

	def setName(self, name):
		self.Name = name

	def clientStart(self):
		self.connection_status = 'none'
		self.clientTCP = socket.socket()
		self.clientTCP.connect((self.hostServer, self.port))

		self.clientTCP.setblocking(0)
		timeout0 = time.clock()

		data = str()

		self.checkStatus('Trying to connect...')

		while True:
				if time.clock()-timeout0 >= 20:
					timeout = True
					break
				else:
					timeout = False
					try:
						data = self.clientTCP.recv(1024)
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
			return 'timeout'
		else:
			if self.connection_status == 'Connected as principal':
				return 'done: principal'
			else:
				return 'done: not principal'
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def NameSend(self):
		print('Waiting to send Name')
		while True:
			try:
				wait_name = self.clientTCP.recv(1024)
				if wait_name == 'send your name'.encode():
					self.clientTCP.send(str(self.Name).encode())
					print('Name sent')
					break
			except: pass
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def checkStatus(self, value):
		self.connection_status = value
		print(value)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def closeConnection(self):
		self.clientTCP.send('close'.encode())
#----------------------------------------------------------------------------------------------------------------------------------------------------------------		
	def sendMyTeam(self, team): #blue, red or random
		print('Waiting to send my team...')	
		while True:
			try:
				wait_team = self.clientTCP.recv(1024)
				if wait_team == 'send your team'.encode():
					self.clientTCP.send(str(team).encode())
					break
			except: pass

		print("Team sent")
		print('Waiting team confirmation...')
		while True:
			try:
				team = self.clientTCP.recv(1024)
				team2 = str(team).split("'")
				team3 = str(team2[0]).split('"')
				self.myteam = str(team3[1])
				self.teamsDisplay = (team2[1], team2[2])
				break
			except: pass
		print('Got my team')
		return 'got my team'
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def myTeam(self):
		return self.myteam
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def displayTeam(self):
		return self.teamsDisplay
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def StartGame(self):
		self.clientTCP.send('start game'.encode())
		self.waitStart()

	def waitStart(self):
		while True:
			try:
				data = self.clientTCP.recv(1024)
				if data == 'start'.encode():
					break
			except: pass
		print('started')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def sendPackages(self, value):
		self.totalclicks(int(value))
		self.clientTCP.send((self.Name + "'" + str(value)).encode())

	def totalclicks(self, value):
		self.myclicks = value

	def receivePoints(self):
		while True:
			try:
				percentage = self.clientTCP.recv(1024)
				print(percentage)
				if percentage == 'game ended'.encode() or percentage == 'restart game'.encode():
					self.getHighScore()
					break
				break
			except: pass
		return percentage

	def getHighScore(self):
		print('Waiting Highscore...')
		while True:
			try:
				self.highscore = self.clientTCP.recv(1024)
				break
			except: pass

	def myHighscore(self):
		return self.highscore

	def endServer(self):
		self.clientTCP.send('close'.encode())
		self.clientTCP.close()

# client = Client()
# client.setHost('127.0.0.1')
# client.setName('Guizaum')
# contador = 0
# breakwhile = False

# while breakwhile == False:
# 	value = client.clientStart()
# 	receiveKill = False

# 	def SEND1():
# 		for i in range(0, 10):
# 				client.sendPackages(1)
# 				time.sleep(.5)
# 		global contador		
# 		contador += 1
# 		if contador == 3:
# 			client.endServer()
# 		else:
# 			client.restartGame()
				
# 		receiveKill = True	

# 	def SEND2():
# 		for i in range(0, 10):
# 				client.sendPackages(1)
# 				time.sleep(.5)

# 	def RECEIVE():
# 		receiveDone = False
# 		while True:
# 			value = client.receivePoints()
# 			print(str(value))
# 			if value == 'game ended'.encode() or value == 'restart game'.encode():# or receiveKill:
# 				break

# 		print(client.myHighscore())

# 		if value == 'game ended'.encode():
# 			global breakwhile
# 			beakwhile = True	

# 	if value == 'done: principal':
# 		time.sleep(10)
# 		client.closeConnection()
# 		client.NameSend()
# 		value = client.sendMyTeam('blue')
# 		if value == 'got my team':
# 			print(client.myTeam())
# 			print(client.displayTeam())
# 			client.StartGame()
# 			t1 = Thread(target=SEND1)
# 			t2 = Thread(target=RECEIVE)
# 			t1.start()
# 			t2.start()
# 	else:
# 		client.NameSend()
# 		value = client.sendMyTeam('blue')
# 		if value == 'got my team':
# 			print(client.myTeam())
# 			print(client.displayTeam())
# 			client.waitStart()
# 			t1 = Thread(target=SEND2)
# 			t2 = Thread(target=RECEIVE)
# 			t1.start()
# 			t2.start()

# client.clientTCP.close()