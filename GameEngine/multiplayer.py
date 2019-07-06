import socket
import threading.Threading
from multiprocessing import Queue
from datetime import datetime
from lib import portforwardlib as pf
from lib import logger


UID_LENGTH = 10


class Multiplayer:
    
    def __init__(self, host="0.0.0.0", port="12345", players={}, log=logger.Logger(), timeout=10, forward=True):
        self.running = True
        
        self.connManager = None

        self.host = host
        self.port = port
        self.players = players
        self.log = log
        self.timeout = timeout
        self.forward = forward

        self.main_socket = None
        self.connected = {}
        self.connected_lock = threading.Threading.RLock
        self.openConnection()

        self.garbageCollect = threading.Thread(target=garbageCollector, args=(self,), daemon=True)
        self.garbageCollect.start()


    def getTime(self):
        return datetime.datetime.utcnow()


    def idGenerator(self, id_length):
        string_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        result = ""

        for x in range(0, id_length):
            result += random.choice(string_list)

        return result


    def garbageCollector(self):
        while self.running:
            
            self.connected_lock.acquire()
            time = self.getTime()
            
            for connId in self.connected:
                dtime = (time - self.connected[connId]["date"]).total_seconds()
                if dtime > self.timeout:
                    self.closeUserConnection(connId)

            self.connected_lock.release()
                

    def openConnection(self):   ## Opens the listening socket
        try:
            self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.main_socket.bind((self.host, self.port))
            self.main_socket.listen()

            if self.forward:
                pf.forwardPort(eport=self.port, iport=self.port, protocol="TCP", time=50000, description="HoA Server listening port")
            
            self.connManager = threading.Thread(target=connectionManager, args=(self,), daemon=True)
            self.connManager.start()
        except(Exception) as err:
            self.main_socket = None

    def connectionManager(self):
        while self.running:
            conn, addr = self.main_socket.accept()
            connId = self.idGenerator(CONNID_LENGTH)
            try:
                
                self.connected_lock.acquire()
                self.connected.update({connId : {}}) ## Adding a dict with the key connId in self.connected
                self.connected[connId].update({"conn" : conn})
                self.connected[connId].update({"ip" : addr[0]})
                self.connected[connId].update({"port" : addr[1]})
                self.connected[connId].update({"date" : self.getTime()})
                self.connected_lock.release()
            except(Exception):
                self.log.log("An error occured while accepting a connection.", "error")

    def closeUserConnection(self, connId):
        self.connected_lock.acquire()
        try:
            self.log.log("Closing the connection with the uid : {}".format(connId), "info")
            self.connected[connId]["conn"].close()
            self.connected.pop(connId)
            self.log.log("Closed connection with the uid : {}".format(connId), "info")
        except(Exception):
            self.log.log("An error occured while trying to close the connection with the uid : {}".format(connId), "error")
        self.connected_lock.release()


    def __del__(self):
        self.running = False

        for connId in self.connected:
            self.closeUserConnection(connId)
