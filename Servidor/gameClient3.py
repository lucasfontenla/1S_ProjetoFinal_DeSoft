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
		self.connectionDone = self.sendInfos = self.InfosSent = self.retryConnection =  False
		self.Wait = True
		
		while not self.closeAll:
			if not self.connectionDone and not self.retryConnection:
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
					self.connectionDone = True

				print('Waiting to send')
				while not self.closeAll:
					try:
						data = self.clientTCP.recv(1024)
						if data == 'connection closed'.encode():
							break
					except: pass	

			if self.connectionDone and self.sendInfos and not self.InfosSent:
				print('Sending name...')
				self.clientTCP.send('sending my name'.encode())
				time.sleep(.1)
				self.clientTCP.send(str(self.setName).encode())
				print('Name sent')
				time.sleep(.1)

				print('Sending my team...')
				self.clientTCP.send('sending my team'.encode())
				time.sleep(.1)
				self.clientTCP.send(str(self.myteam).encode())
				print('Team sent')
				
				self.Wait = True
				print('Waiting start...')	
				while not self.closeAll:
					try:
						data = self.clientTCP.recv(1024)
						if data == 'start'.encode():
							break
					except: pass
				print('started')
				self.Wait = False
				break

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def SendInfos(self):
		self.sendInfos = True
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
		return self.Wait
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