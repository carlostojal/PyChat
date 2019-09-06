import socket
from client_distribute import *

#
# Copyright (c) Carlos Tojal (carlostojal)
# client_receive.py
# PyChat
# github.com/carlostojal/PyChat
#

s = socket.socket()

print("** PyChat Client **")
print("** Receiver **")
host = input("Server IP address: ")
port = input("Server port: ")

# connects to server
s.connect((host, int(port)))


configure_question = input("Will another client connect with you (y/n)? ")
if configure_question == "y":
    configure_distributor()
    configured_distributor = True
else:
    configured_distributor = False

print("\n")

# receives messages from server
while True:
    message = s.recv(1024).decode()
    if message:
        print(message)
    if configured_distributor:
        distribute(message)


