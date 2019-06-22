from lib import portforwardlib as pf


class Multiplayer:
    
    def __init__(self, host="0.0.0.0", port="12345", players):

        self.connection = {}
        self.connection.update({"host":host}, {"port":port})

        self.players = players
