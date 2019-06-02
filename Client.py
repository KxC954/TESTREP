import socket
import sys
import threading

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            #msg = Message()
            self.sock.send(bytes(input(""), "utf-8"))

    def __init__(self, address):
        self.sock.connect((address, 10000))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        print("Connected to "+address+".")
        while True:
            data = self.sock.recv(1024)
            print(data.decode("utf-8"))
            if not data:
                break

ip = input("Ip ?:")
client = Client(ip)
