import socket, time
from random import randint

#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte

class Server():
	def __init__(self):
		self.host = '127.0.0.1' #[ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][1] #pega o IP da máquina
		self.port = 5000 #a porta da conexão é a porta 80 web

	def serverStart(self):	#a função inicia o servidor
		print("Servidor Iniciado")
		print('Server IP: ', self.host)
		self.clients_connected = list()

		self.s = socket.socket()
		self.s.bind((self.host, self.port))

		self.s.listen(1)
		self.s.setblocking(0)

		while True: #escuta os clientes
			try:
				c, addr = self.s.accept()
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
					else:
						pass
				except:
					pass

		print("end")
		self.sortTeams()

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
			else:
				continue

		self.sendTeams()

	def sendTeams(self):
		for blue in self.team_blue:
			blue[0].send('team blue'.encode())

		for red in self.team_red:
			red[0].send('team red'.encode())
		print("Team Red: ", self.team_red)
		print("Team Blue: ", self.team_blue)
		self.waitStart()

	def waitStart(self): 
		while True:
			try:
				print('Waiting')
				data = (self.clients_connected[0][0]).recv(1024)
				if data:
					if data == 'start game'.encode():
						break
				else:
					pass
			except:
				pass

		print('Starting game')
		self.sendStart()

	def sendStart(self):
		time.sleep(.5) #"re-bounce"
		for client in self.clients_connected:
			client[0].send('start'.encode())
		print('Game started')
		self.receivePackages()

	def receivePackages(self):
		listaqqr = list()
		while True:
			whilebreak = False
			for i in range(2, len(self.clients_connected)-1):
				try:
					pack = (self.clients_connected[0][i]).recv(1024)
					listaqqr.append(str(pack))
					print(str(pack))
					if pack == 'end server'.encode():
						whilebreak = True
						break
					else:
						pass
				except:
					pass

			if whilebreak:
				break
		print(len(listaqqr))
		self.s.close()

server = Server()
server.serverStart()