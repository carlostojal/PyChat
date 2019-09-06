import socket
from distributing import *

#
# Copyright (c) Carlos Tojal (carlostojal)
# receiving.py
# PyChat
# github.com/carlostojal/PyChat
#

s = socket.socket()


def configure_receiver():
    print("** PyChat Client **")
    print("** Receiver **")
    host = input("Server IP address: ")
    port = input("Server port: ")

    s.connect((host, int(port)))


def configure_distributor_receiving():
    configure_question = input("Will another client connect with you (y/n)? ")
    if configure_question == "y":
        print("Run distribute.py and configure the connection.")
        configured_distributor = True
    else:
        configured_distributor = False
    print("\n")

    return configured_distributor


def receive(configured_distributor):
    while True:
        message = s.recv(1024).decode()
        if not message:
            break
        if message:
            print(message)
        if configured_distributor:
            distribute(message)
