import time, socket
from threading import Thread
from random import randint  

#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte 

class Client():
	def __init__(self):
		self.closeAll = False
		self.port = 80
		self.connection_status = 'none'
		self.percentage = .5

	def showMyHost(self): 
		try:
			IP = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][1] #arrumar para todos pcs try except
		except:
			IP = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]
		return IP

	def setHost(self, serverIP): #OK
		self.hostServer = serverIP

	def setName(self, name): #OK
		self.Name = name

	def clientStart(self): #OK
		print('Client Starting...')
		self.clientTCP = socket.socket()
		try:
			self.clientTCP.connect((self.hostServer, self.port))
		except: pass

		self.clientTCP.setblocking(0)
		timeout0 = time.clock()

		data = str()

		self.checkStatus('Trying to connect...')

		while not self.closeAll:
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
			self.checkStatus('Timeout')
			return 'timeout'
		else:
			if self.connection_status == 'Connected as principal':
				return 'done: principal'
			else:
				return 'done: not principal'
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def waitToSend(self):
		print('Waiting to send')
		while True:
			try:
				data = self.clientTCP.recv(1024)
				if data == 'connection closed'.encode():
					break
			except: pass		

	def NameSend(self):
		print('Sending name...')
		self.clientTCP.send('sending my name'.encode())
		time.sleep(.1)
		self.clientTCP.send(str(self.setName).encode())
		print('Name sent')
		self.sendMyTeam()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def checkStatus(self, value):
		self.connection_status = value
		print(value)

	def Status(self):
		return self.connection_status
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def closeConnection(self):
		self.clientTCP.send('close'.encode())
#----------------------------------------------------------------------------------------------------------------------------------------------------------------		
	def setTeam(self, team):
		if team == 'random':
			number = randint(0, 1)
			if number == 0:
				team = 'blue'
			else:
				team = 'red'
		self.myteam = team

	def sendMyTeam(self):
		print('Sending my team...')
		self.clientTCP.send('sending my team'.encode())
		time.sleep(.1)
		self.clientTCP.send(str(self.myteam).encode())
		print('Team sent')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def displayTeams(self):
		self.clientTCP.send('update players'.encode())
		with self.setblocking(1):
			update = self.clientTCP.recv(1024)
		update2 = str(update).split("'")
		update3 = str(update).split("][")
		redUp = (str(update3).split("["))[1].split(",")
		blueUp = (str(update3).split("]"))[2].split(",")
		print(redUp, blueUp)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def StartGame(self):
		print('Sending start...')
		self.clientTCP.send('start game'.encode())
		print('Start sent')
		self.waitStart()

	def waitStart(self):	
		print('Waiting start...')	
		while not self.closeAll:
			try:
				data = self.clientTCP.recv(1024)
				break
			except: pass
		print('started')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def sendPackages(self, value):
		self.totalclicks(int(value))
		self.clientTCP.send((str(value)).encode())
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def totalclicks(self, value):
		self.myclicks = value
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def receivePoints(self):
		while not self.closeAll:
			try:
				self.percentage = self.clientTCP.recv(1024)
				print(percentage)
				if self.percentage == 'client close game'.encode() or self.percentage == 'client restart game'.encode():
					self.getHighScore()
					break
			except: pass
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def getPercentage(self):
		return self.percentage

	def getHighScore(self):
		print('Waiting Highscore...')
		while not self.closeAll:
			try:
				self.highscore = self.clientTCP.recv(1024)
				break
			except: pass

	def myHighscore(self):
		return self.highscore

	def endServer(self):
		self.clientTCP.send('close'.encode())
		self.Close()

	def Close(self):
		self.closeAll = True
		print('Client Closed')
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