import socket

#
# Copyright (c) Carlos Tojal (carlostojal)
# client_send.py
# PyChat
# github.com/carlostojal/PyChat
#

s = socket.socket()


def configure():
    print("\n** PyChat Client **")
    print("** Sender Configuration **")
    print("Your IP Address: ", socket.gethostbyname(socket.gethostname()))

    server_address = input("\nServer IP Address: ")
    server_port = input("Server Port: ")

    s.connect((server_address, int(server_port)))


def chat():
    username = input("\nUsername: ")
    print("\n ")
    message_content = ""
    while message_content != "exit":
        message_content = input("Your message: ")
        if message_content != "":
            message = username+": "+input("Your message: ")
            send(message)
        else:
            print("Message can't be empty.")


def send(message):
    s.send(message.encode())


