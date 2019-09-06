import socket
from client_send import send

#
# Copyright (c) Carlos Tojal (carlostojal)
# client_distribute.py
# PyChat
# github.com/carlostojal/PyChat
#

s = socket.socket()

host = socket.gethostbyname(socket.gethostname())

print("** Distributor Configuration **\n")
print("Insert below a different port from the one that you used to connect to the server.")
print("This is the port that the next client will use to connect to you.\n")
port = input("Your port: ")

s.bind((host, int(port)))

global sender, sender_addr
global receiver, receiver_addr


# configures distributor
def configure_distributor():
    print("Waiting for connection...")
    s.listen()

    sender, sender_addr = s.accept()
    print("Got sender connection from ", sender_addr)
    receiver, receiver_addr = s.accept()
    print("Got receiver connection from ", receiver_addr)
    print("\n")


def upload():
    message = s.recv(1024)
    send(message)


# distributes message to next client
def distribute(message):
    receiver.send(message.encode())
    print("(Distributed  message to ", receiver_addr, ")")
