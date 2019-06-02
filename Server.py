import socket
import sys
import threading

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.sock.bind(("0.0.0.0", 10000))
        self.sock.listen(1)
        print("Server running, waiting for connection...")

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(bytes(str((str(a[0]) + ":" + str(a[1]) + " said: " +
                                           str(data.decode("utf-8")))), "utf-8"))

            print(str(a[0]), ":", str(a[1]), "said :" + str(data.decode("utf-8")))

            if not data:
                print(str(a[0]), ":", (a[1]), " has left the chat")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = False
            cThread.start()
            self.connections.append(c)
            print(str(a[0]), ":", (a[1]), " joined the chat")

server = Server()
server.run()