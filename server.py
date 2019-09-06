import socket

#
# Copyright (c) Carlos Tojal (carlostojal)
# server.py
# PyChat
# github.com/carlostojal/PyChat
#

s = socket.socket()

host = socket.gethostbyname(socket.gethostname())
port = 0

print("\n** PytChat Server **\n")
print("IP Address: ", host)
port = input("Port: ")

s.bind((host, int(port)))
s.listen()

print("\nServer started")

sender, sender_addr = s.accept()
print("Got sender connection from ", sender_addr)
receiver, receiver_addr = s.accept()
print("Got receiver connection from ", receiver_addr)

while True:
    data = sender.recv(1024).decode()
    if not data:
        break
    print(data)
    receiver.send(data.encode())
