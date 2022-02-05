import socket
import _thread


connection = None

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    global connection
    connection = socket.socket()  # instantiate
    connection.connect((host, port))  # connect to the server

    _thread.start_new_thread(incoming_message_thread, ())
    #_thread.start_new_thread(outgoing_message_thread, ())

    while True:
        pass


def incoming_message_thread():
    while True:
        message = connection.recv(1024).decode()
        print("Recieved: " + message)

def outgoing_message_thread():
    while True:
        message = input(' -> ')
        connection.send(message.encode())



if __name__ == '__main__':
    client_program()