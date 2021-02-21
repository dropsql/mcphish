import threading
import socket
import sys

from lib.fowarder import foward
from lib.prints import *

class Server:
    def __init__(self, lhost: str, lport: int, rhost: str, rport: int):
        self.lhost = lhost
        self.lport = lport
        self.rhost = rhost
        self.rport = rport

        super().__init__()

    def start(self):
        self.run()

    def listen(self):
        self.run()

    def run(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.server_socket.bind((self.lhost, self.lport))
        except:
            print_error('can\'t bind port to %s:%s' % (self.lhost, self.lport))
            sys.exit(-1)

        print_info('server is listening on %s:%s' % (self.lhost, self.lport))
        self.server_socket.listen(1337)

        while True:
            self.local_socket, self.local_addr = self.server_socket.accept()
            print_info('got a connection from %s:%s, redirecting to %s:%s' % (self.local_addr[0], self.local_addr[1], self.rhost, self.rport))

            self.remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                self.remote_socket.connect((self.rhost, self.rport))
            except:
                print_error('can\'t connect to %s:%s' % (self.rhost, self.rport))
                sys.exit(-1)

            threading.Thread(
                target=foward, 
                args=(self.remote_socket, self.local_socket, False)
            ).start()

            threading.Thread(
                target=foward, 
                args=(self.local_socket, self.remote_socket, True)
            ).start()
            print_success('bridge started! %s:%s <=> %s:%s' % (self.local_addr[0], self.local_addr[1], self.rhost, self.rport))
