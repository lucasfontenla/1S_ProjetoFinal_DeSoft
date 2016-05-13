import socket, time
from random import randint

#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte

class Server():
	def __init__(self):
		self.host = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][1] #pega o IP da máquina
		self.port = 80 #a porta da conexão é a porta 80 web

	def serverStart(self):	#a função inicia o servidor
		print("Servidor Iniciado")
		print('Server IP:', self.host)
		self.clients_connected = list()

		self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server.bind((self.host, self.port))
		self.server.setblocking(0)

		self.generalDict = dict()

		while True: #escuta os clientes
			try:
				data_in, addr = self.server.recvfrom(1024)
				data = str(data_in).split(':')
				print(data)
				if data[1] == "hello server'":
					if not addr in self.clients_connected:
						self.clients_connected.append(addr)
						self.addDict(addr, data[0])
						if self.clients_connected[0] == addr:
							self.server.sendto('connected as principal'.encode(), addr) #envia pro cliente principal
							print('Principal:', addr)
						else:	
							self.server.sendto('connected'.encode(), addr)
							print(addr)
				elif data_in == ':close'.encode():
					if addr == self.clients_connected[0]:
						break 
			except: pass

		print("end")
		print(self.generalDict)
		self.sortTeams()

	def addDict(self, addr, name_in):
		name = name_in.split("'")
		self.generalDict[addr] = name[1]

	#sorteia os timeas aleatóriamente
	def sortTeams(self):
		self.team_blue = list()
		self.team_red = list()
		players = self.clients_connected[:]
		number = randint(0, 1)

		for player in players:
			if number == 0:
				self.team_blue.append(player)
				number = 1
			else:
				self.team_red.append(player)
				number = 0
			if (len(self.team_blue)+len(self.team_red)) == len(players):
				break
		print(self.team_red, self.team_blue)
		self.sendTeams()

	def sendTeams(self):
		time.sleep(.5) #'re-bounce'
		for blue in self.team_blue:
			self.server.sendto('team blue'.encode(), blue)

		for red in self.team_red:
			self.server.sendto('team red'.encode(), red)
		print("Team Red: ", self.team_red)
		print("Team Blue: ", self.team_blue)
		self.waitStart()

	def waitStart(self): 
		print('Waiting')
		self.server.setblocking(1)
		while True:
			data, addr = self.server.recvfrom(1024)
			if data:
				if addr == self.clients_connected[0]:
					if data == 'start game'.encode(): break

		print('Starting game')
		self.sendStart()

	def sendStart(self):
		time.sleep(.5) #"re-bounce"
		for client in self.clients_connected:
			self.server.sendto(('start'.encode()), client)
		print('Game started')
		self.receivePackages()

	def receivePackages(self):
		self.initial_time = time.clock()
		self.pointsRED = 0
		self.pointsBLUE = 0
		self.highscore_blue = dict()
		self.highscore_red = dict()
		self.server.setblocking(0)
		recived = False
		while True:
			try:
				pack, addr = self.server.recvfrom(1024)
				print('recv', pack)
				if pack == 'stop receiving'.encode():
					print('stopped receiving')
					break
				else:
					team = self.checkTeam(addr)
					self.addPack(team, addr, str(pack))
					recived = True
			except: pass

			if 0 <= ((time.clock()-self.initial_time)%.5) <= .1 and recived:
				self.sendREDClients(self.totalRed())
				self.sendBLUEClients(self.totalBlue())

		print(self.totalBlue(), self.totalRed())
		print(self.gameHighScore())
#		self.sendHighScore()

	def checkTeam(self, addr):
		if addr in self.team_blue:
			return 'blue'
		elif addr in self.team_red:
			return 'red'

	def addPack(self, team, addr, pack):
		pack2 = pack.split("'")
		if team == 'blue':
			self.pointsBLUE = self.pointsBLUE + int(pack2[1])
#			self.addHighScore(team, addr, int(pack2[1]))
		elif team == 'red':
			self.pointsRED = self.pointsRED + int(pack2[1])
#			self.addHighScore(team, addr, int(pack2[1]))

	def totalRed(self):
		percentage = (self.pointsRED/(self.pointsBLUE+self.pointsRED))
		return (str(percentage))

	def totalBlue(self):
		percentage = (self.pointsBLUE/(self.pointsRED+self.pointsBLUE))
		return (str(percentage))

	def sendREDClients(self, value):
		for client in self.team_red:
			self.server.sendto(str(value).encode(), client)

	def sendBLUEClients(self, value):
		for client in self.team_blue:
			self.server.sendto(str(value).encode(), client)

	def addHighScore(self, team, addr, pack):
		search = self.generalDict[addr]
		if team == 'blue':
			if not search in self.highscore_blue.keys():
				self.highscore_blue[search] = pack
			else:
				self.highscore_blue[search] = self.highscore_blue[search] + pack
		elif team == 'red':
			if not search in self.highscore_red.keys():
				self.highscore_red[search] = pack
			else:
				self.highscore_red[search] = self.highscore_red[search] + pack

	def gameHighScore(self):
		return (self.highscore_blue, self.highscore_red)

	def sendHighScore(self):
		time.sleep(.5) #"re-bounce"
		for client in self.clients_connected:
			self.server.sendto(str(self.gameHighScore()).encode, client)
		print('HighScore Sent')

print("ok")		
server = Server()
server.serverStart()