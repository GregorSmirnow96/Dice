from mBoard import Board
from _Game import Game
from _Player import Player
from _Session import Session
import socket
from threading import Thread


def start():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    max_clients_allowed = 2
    players = []
    while len(players) < max_clients_allowed:
        server_socket.listen(max_clients_allowed)
        
        connection, address = server_socket.accept()
        print("Connection from: " + str(address))
        client_session = Session(connection, address)
        client_session.start()

        player = Player(client_session, Board())
        players.append(player)
    
    game_is_active = True # This should change dynamically.
    game = Game(players)
    game.start()



if __name__ == '__main__':
    start()
