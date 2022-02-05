from threading import Thread
from queue import Queue


class Session:

    def __init__(self,
        connection,
        address):
        self.connection = connection
        self.address = address

        self.keep_alive = True
        self.upstream_connection = _ClientMessageListener(self)
        self.downstream_connection = _ClientMessageSender(self)

    def start(self):
        print("Session begining for: " + str(self.address))
        self.upstream_connection.start()
        self.downstream_connection.start()
    
    def end(self):
        self.connection.close()
        self.keep_alive = False
        self.downstream_connection.keep_alive = False
        self.upstream_connection.keep_alive = False
    
    def send_message(self, message):
        self.downstream_connection.messages.put(message)

    def get_message(self,
        prefix='',
        max_wait=None):
        import time
        if max_wait:
            start_time = time.time()
            current_time = time.time()
            while current_time - start_time < max_wait:
                for message in self.upstream_connection.messages.queue:
                    if message.startswith(prefix):
                        self.upstream_connection.messages.queue.remove(message)
                        return message
                current_time = time.time()
            return None

        if self.upstream_connection.messages.qsize() == 0:
            return None
        
        for message in self.upstream_connection.messages.queue:
            if message.startswith(prefix):
                self.upstream_connection.messages.queue.remove(message)
                return message
        
        return None

class _ClientMessageListener(Thread):

    def __init__(self, session):
        Thread.__init__(self)
        self.session = session
        self.keep_alive = True
        self.messages = Queue()
        self.messages.put('DRAFT:TAKE_TURN4')
        self.messages.put('DRAFT:TAKE_TURN5')
    
    def run(self):
        while self.keep_alive:
            incoming_message = self.session.connection.recv(1024).decode()
            if incoming_message:
                print("Incoming from: " + str(self.session.address) + " -> " + incoming_message)
                self.messages.put(incoming_message)


class _ClientMessageSender(Thread):

    def __init__(self, session):
        Thread.__init__(self)
        self.session = session
        self.keep_alive = True
        self.messages = Queue()
    
    def run(self):
        while self.keep_alive:
            if self.messages.qsize() == 0:
                continue

            outgoing_message = self.messages.get()
            self.session.connection.send(outgoing_message.encode())
            print("Outgoing to: " + str(self.session.address) + " -> " + outgoing_message)
