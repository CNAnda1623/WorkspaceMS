import threading
import socket
import argparse
import os

class Server(threading.Thread):
    def __init__(self,host,port):
        super().__init__()
        self.connections = []
        self.host = host
        self.port = port

    def run(self):
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR)
        sock.bind((self.host , self.port))

        sock.listen(1)
        print("Listening at",sock.getsockname())

        while True:
            #Accepting new connection
            sc, sockname = sock.accept()
            print(f"Accepting a new connection from {sc.getpeername()} to {sc.getsockname()}")
            #Create a new thread
            server_socket = ServerSocket(sc , sockname , self)
            # Start a new Thread
            server_socket.start()
            # Add thread to active connection
            self.connections.append(server_socket)
            print("Ready to recieve messages from",sc.getpeername())

    def broadcast(self , message , source):
        for connection in self.connections:
            # Send to all connected client accept the source client
            if connection.sockname != source:
                connection.send(message)

    def remove_connection(self , connection):
        self.connections.remove(connection)

class ServerSocket(threading.Thread):

    def __init__(self , sc , sockname , server):
        super().__init__()
        self.sc = sc
        self.sockname = sockname
        self.server = server

    def run(self):
        while True:
            message = self.sc.recv(1024).decode('ascii')

            if message:
                print(f"{self.sockname} says {message}")
                self.server.broadcast(message , self.sockname)
            else:
                print(f"{self.sockname} has closed the connection")
                self.sc.close()
                server.remove_connection(self)
                return

    def send(self , message):
        self.sc.sendall(message.encode('ascii'))

def exit(server):
    while True:
        ipt = input("")
        if ipt == "q":
            print("Closing all connections...")
            for connection in server.connections:
                connection.sc.close()
            print("Shutting down the server....")
            os.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chatroom Server")
    parser.add_argument('host' , help='Interace the server listens at')
    parser.add_argument('-p' , metavar='Port' , type=int , default=1060 , help='TCP port(default 1060)')

    args = parser.parse_args()

    # Create and start server thread
    server = Server(args.host , args.p)
    server.start()

    exit = threading.Thread(target=exit , args= (server,))
    exit.start()