import socket, time
from threading import Thread #threads geram "microservers" que computam a pontuação de cada usuário
from random import randint

#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte

class Server():
	def __init__(self):
		try:
			self.host = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][1] #arrumar para todos pcs try except
		except:
			self.host = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]  #pega o IP da máquina
		self.port = 80 #a porta da conexão é a porta 80 web (sempre aberta, não precisa)

	def serverStart(self):	#a função inicia o servidor
		print("Servidor Iniciado")
		print('Server IP:', self.host, '\n')
		self.clients_connected = list()

		self.servertcp = socket.socket() #A conexão estabelecida é TCP
		self.servertcp.bind((self.host, self.port)) 

		self.servertcp.listen(1)
		self.servertcp.setblocking(0)

		while True: #escuta os clientes
			try:
				c, addr = self.servertcp.accept()
				if not (c, addr) in self.clients_connected:
					self.clients_connected.append((c, addr))
					print(addr)
					if self.clients_connected[0] == (c, addr):
						c.send('connected as principal'.encode()) #envia pro cliente principal
					else:	
						c.send('connected'.encode())
			except:
				try:
					data = self.clients_connected[0][0].recv(1024) #o cliente pricipal pode fazer o servidor parar de escutar por jogadores
					if data == 'close'.encode():
						break
				except: pass

		print("Open connection ended")
		self.callforNames()

	def callforNames(self):
		receivePlease = Thread(target=self.receiveTeams)
		receivePlease.start()

		self.NameDict = dict()
		print('Getting names...')
		for client in self.clients_connected:
			client[0].send('send your name'.encode())
			while True:
				try:
					name = client[0].recv(1024)
					name2 = str(name).split("'")
					self.NameDict[client] = [str(name2[1])]
					print(str(name), 'playing')
					break
				except: pass

	def receiveTeams(self):	
		self.ReceiveThreadsDone = 0
		self.team_blue = list()
		self.team_red = list()
		self.random_List = list()
		self.blueDict = dict()
		self.redDict = dict()
		self.generalDict = dict()

		for client in self.clients_connected:
			self.generalDict[client[0]] = Thread(target=self.separateTeams, args=(client,))
			self.generalDict[client[0]].start()

		while True:
			if self.ReceiveThreadsDone == len(self.clients_connected):
				break
		self.sendTeams()

	#sorteia os times aleatóriamente
	def separateTeams(self, client):		
		while True:
			try:
				team = client[0].recv(1024)
				team2 = str(team).split("'")
				
				if team2[1] == 'blue':
					self.team_blue.append(client)
					self.NameDict[client].append('blue')
					self.blueDict[self.NameDict[client][0]] = 0

				elif team2[1] == 'red':
					self.team_red.append(client)
					self.NameDict[client].append('red')
					self.redDict[self.NameDict[client][0]] = 0

				elif team2[1] == 'random':
					self.random_List.append(client)
				break
			except: pass

		for client in self.random_List:		
			if len(self.team_blue) < len(self.team_red):
				self.team_blue.append(client)
				self.NameDict[client].append('blue')
				self.blueDict[self.NameDict[client][0]] = 0

			elif len(self.team_red) < len(self.team_blue):
				self.team_red.append(client)
				self.NameDict[client].append('red')
				self.redDict[self.NameDict[client][0]] = 0

			else:
				number = randint(0, 1)
				if number == 0:
					self.team_blue.append(client)
					self.NameDict[client].append('blue')
					self.blueDict[self.NameDict[client][0]] = 0
				else:
					self.team_red.append(client)
					self.NameDict[client].append('red')
					self.redDict[self.NameDict[client][0]] = 0		
		self.ReceiveThreadsDone += 1

	def sendTeams(self):
		print('Sending teams...')
		namesBlue = str()
		namesRed = str()

		for lista in self.NameDict.values():
			if lista[1] == 'red':
				namesRed+=":"+lista[0]
			else:
				namesBlue+=":"+lista[0]

		for blue in self.team_blue:
			toSend = 'team blue'+"'"+namesBlue+"'"+namesRed
			blue[0].send(str(toSend).encode())

		for red in self.team_red:
			toSend = 'team red'+"'"+namesRed+"'"+namesBlue
			red[0].send(str(toSend).encode())

		print("Team Red: ", self.team_red)
		print("Team Blue: ", self.team_blue)
		self.waitStart()

	def waitStart(self): 
		print('Waiting the game Start')
		while True:
			try:
				data = (self.clients_connected[0][0]).recv(1024)
				if data:
					if data == 'start game'.encode():
						break
			except: pass

		print('Starting game')
		self.sendStart()

	def sendStart(self):
		time.sleep(1) #"re-bounce"
		for client in self.clients_connected:
			client[0].send('start'.encode())
		print('Game started')
		self.killThreads = False
		self.generalDict = dict()
		self.doneThreads = 0
		self.receiving()

	def receiving(self):
		print('Receiving')
		for client in self.clients_connected:
			if client in self.team_red:
				team = 'red'
			else:
				team = 'blue'
			self.generalDict[client[0]] = Thread(target=self.receivePackages, args=(client, team))
			self.generalDict[client[0]].start()
		self.gameEnded()

	def receivePackages(self, player, team):
		initial_time = time.clock()
		self.pointsRED = 0
		self.pointsBLUE = 0
		self.servertcp.setblocking(0)
		my_points = 0

		self.restart = False

		while True:
			if 0 <= (time.clock()-initial_time)%.5 <= .005:
				player[0].send(self.totalPoints().encode())
				print('Sending', self.totalPoints())

			if self.killThreads:
				break

			try:
				pack = player[0].recv(1024)
				print(pack)
				if pack == 'restart game'.encode():
					self.restart = True
					self.killThreads = True
					break
				elif pack == 'close'.encode():
					self.restart = False
					self.killThreads = True
				else:
					pack2 = str(pack).split("'")
					pack3 = pack2[1].split('"')
					name = pack2[0].split("'")
					my_points += int(pack3[0])
					if team == 'blue':
						self.addPack('blue', str(pack3[0]))
					elif team == 'red':
						self.addPack('red', str(pack3[0]))
			except: pass

		if team == 'blue':
			self.addBlueDict(player, my_points)
		elif team == 'red':
			self.addRedDict(player, my_points)

		self.doneThreads += 1

	def gameEnded(self):
		num_players = len(self.clients_connected)
		while True:
			if self.doneThreads == num_players:
				print(self.pointsRED, self.pointsBLUE)	
				print(self.NameDict.values())
				print(self.blueDict, self.redDict)
				break

		print('Sending Highscore...')

		if self.restart:
			toSend = 'restart game'
		else:
			toSend = 'game ended'

		print('Game status: ', toSend)	

		for player in self.clients_connected:
			player[0].send(toSend.encode())
			time.sleep(.1)
			player[0].send((str(self.blueDict)+"!!"+str(self.redDict)).encode())

		print('Highscore sent')

		if self.restart:
			print('Restarting Game...')
			self.restartGame()
		else:
			print('Ending game...')
			print('Closing server...')
			self.servertcp.close()
			print('Server Closed')

	def addPack(self, team, pack):
		if team == 'blue':
			self.pointsBLUE = self.pointsBLUE + int(pack)
		elif team == 'red':
			self.pointsRED = self.pointsRED + int(pack)

	def addBlueDict(self, player, points):
		player_name = self.NameDict[player][0]
		self.blueDict[player_name] = points

	def addRedDict(self, player, points):
		player_name = self.NameDict[player][0]
		self.redDict[player_name] = points

	def totalPoints(self):
		if self.pointsBLUE == 0 or self.pointsRED == 0:
			percentage = .5
		else:
			percentage = (self.pointsRED/(self.pointsBLUE+self.pointsRED))
		return str(percentage)

	def restartGame(self):
		self.pointsRED = 0
		self.pointsBLUE = 0

		for player in self.redDict.keys():
			self.redDict[player] = 0

		for player in self.blueDict.keys():
			self.blueDict[player] = 0

		self.waitStart()

	def Close(self):
		self.servertcp.close()
		print('Server Closed')

#server = Server()
#server.serverStart()