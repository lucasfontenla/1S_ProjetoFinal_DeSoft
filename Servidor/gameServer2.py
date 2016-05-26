import socket, time
from threading import Thread #threads geram "microservers" que computam a pontuação de cada usuário
from random import randint

#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte

class Server():
	def __init__(self):
		self.closeAll = False
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
		while not self.closeAll: #escuta os clientes
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
						for client in self.clients_connected:
							client[0].send('connection closed'.encode())
						break
				except: pass
		print(self.clients_connected)
		print("Open connection ended")

		self.ReceiveThreadsDone = 0
		self.team_blue = list()
		self.team_red = list()
		self.BlueNames = list()
		self.RedNames = list()
		self.blueDict = dict()
		self.redDict = dict()
		self.generalDict = dict()
		self.NameDict = dict()

		self.pointsRED = 0
		self.pointsBLUE = 0
		self.doneThreads = 0

		for client in self.clients_connected:
			self.generalDict[client] = Thread(target=self.serverForClient, args=(client,))
			self.generalDict[client].start()

	def serverForClient(self, client):
		myteam = str()
		mypoints = 0
		print("Server Working")
		while not self.closeAll:
			try:
				data = client[0].recv(1024)

				if data == 'sending my name'.encode(): ##################### Código para enviar o nome
					print("Receiving Name\n")
					while not self.closeAll:
						try:
							name = client[0].recv(1024)
							name2 = str(name).split("'")
							self.NameDict[client] = [str(name2[1])]
							print('Name Received')
							print(str(name2[1]), 'playing')
							break
						except: pass

				elif data == "sending my team".encode(): ##################### Código para enviar o time
					print("Receiving Team\n")
					while not self.closeAll:
						try:
							team = client[0].recv(1024)
							team2 = str(team).split("'")
							if team == 'blue'.encode():
								self.team_blue.append(client)
								self.BlueNames.append(str(name2[1]))
								self.blueDict[str(name2[1])] = 0
							elif team == 'red'.encode():
								team2 = str(team).split("'")
								self.team_red.append(client)
								self.BlueNames.append(str(name2[1]))
								self.redDict[str(name2[1])] = 0
							client[0].send(str(team2[1]).encode())	
							myteam = team2[1]
							print("Team Received")
							print(str(name2[1]), str(myteam))
							break
						except: pass

				elif data == 'update players'.encode(): ##################### Código para receber atualizações sobre os jogadores
					self.updateClient(client)

				elif data == 'start game'.encode(): ##################### Código para começar o jogo
					print('Starting game...')

					for player in self.clients_connected:
						player[0].send('start'.encode())
						print('Sent to {0}'.format(player[1]))

					print('''\n################################################
GAME STARTED
################################################\n''')
					initial_time = time.clock()
					print('Receiving...\n')
					while not self.closeAll:
						if 0 <= (time.clock()-initial_time)%.5 <= .005:
							client[0].send(self.totalPoints().encode())

						try:
							pack = client[0].recv(1024)
							if pack == 'close game'.encode():
								print('Closing game...')
								for player in self.clients_connected:
									player[0].send('client close game'.encode())

							elif pack == 'client close game'.encode():
								print('Game closed')
								self.closeGame = True

							elif pack == 'restart game'.encode(): 
								print('Restart game...')
								if myteam == 'blue':
									self.addBlueDict(client, mypoints)
								else:
									self.addRedDict(client, mypoints)

								player[0].send('client restart game'.encode())
								time.sleep(1000)
								self.sendHighscore()
								break

							elif pack == 'client restart game'.encode():
								print('Game restarted')
								self.closeGame = False
								self.restartValues()
								break

							elif pack == 'update players'.encode():
								self.updateClient(client)

							else:
								pack2 = str(pack).split("'")
								print(name2[1], pack2[1])
								self.addPack(myteam, pack2[1])
								mypoints+=int(pack2[1])
						except: pass

					if self.closeGame:
						self.Close()
						break
			except: pass

		self.gameEnded()
		self.doneThreads += 1

	def updateClient(self, client):
		print('Sending players update...')
		client[0].send((str(self.RedNames)+str(self.BlueNames)).encode())
		print('Update sent')

	def sendHighscore(self):
		print('Sending Highscore...')

		for player in self.clients_connected:
			player[0].send(toSend.encode())
			time.sleep(.1)
			player[0].send((str(self.blueDict)+"!!"+str(self.redDict)).encode())

		print('Highscore sent')

	def gameEnded(self):
		num_players = len(self.clients_connected)
		while not self.closeAll:
			if self.doneThreads == num_players:
				print(self.pointsRED, self.pointsBLUE)	
				print(self.NameDict.values())
				print(self.blueDict, self.redDict)
				break

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

	def Close(self):
		self.closeAll = True
		self.servertcp.close()
		print('Server Closed')

# server = Server()
# server.serverStart()