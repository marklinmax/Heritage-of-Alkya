import socket
from threading import Thread
from multiprocessing import Queue
from lib import portforwardlib as pf


class Multiplayer:
    
    def __init__(self, host="0.0.0.0", port="12345", players):

        self.connManager = None

        self.host = host
        self.port = port

        self.players = players

        self.main_socket = None
        self.openConnection()

        self.connected = {}

        self.running = True

    def openConnection(self):
        try:
            self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.main_socket.bind((self.host, self.port))
            self.main_socket.listen()
            
            self.connManager = Thread(target=connectionManager, args=(self))
            self.connManager.start()
        except(Exception) as err:
            self.main_socket = None

    def connectionManager(self):
        while self.running:
            conn, addr = self.main_socket.accept()
            self.connected.update({"conn" : conn}, {"ip" : addr[0]}, {"port" : addr[1]})
