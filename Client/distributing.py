import socket
from sending import send

#
# Copyright (c) Carlos Tojal (carlostojal)
# distributing.py
# PyChat
# github.com/carlostojal/PyChat
#

receiver = ("127.0.0.1", 255)


def configure_distributor():
    s = socket.socket()
    host = socket.gethostbyname(socket.gethostname())
    print("** Distributor Configuration **\n")
    print("Insert below a different port from the one that you used to connect to the server.")
    print("This is the port that the next client will use to connect to you.\n")
    port = input("Your port: ")
    s.bind((host, int(port)))
    return s


# configures distributor
def configure_client(s):
    print("Waiting for connection...")
    s.listen()

    sender, sender_addr = s.accept()
    print("Got sender connection from ", sender_addr)
    receiver, receiver_addr = s.accept()
    print("Got receiver connection from ", receiver_addr)
    print("\n")


# send message to previous client
def upload(s):
    message = s.recv(1024)
    send(message)


# distributes message to next client
def distribute(message):
    receiver.send(message.encode())
    print("(Distributed  message to ", receiver, ")")
