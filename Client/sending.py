import socket

#
# Copyright (c) Carlos Tojal (carlostojal)
# sending.py
# PyChat
# github.com/carlostojal/PyChat
#

s = socket.socket()


# sending window functions
def configure():
    print("\n** PyChat Client **")
    print("** Sender Configuration **\n")
    print("Your IP Address: ", socket.gethostbyname(socket.gethostname()))

    server_address = input("\nServer IP Address: ")
    server_port = input("Server Port: ")

    global s

    s.connect((server_address, int(server_port)))


def chat():
    username = input("\nUsername: ")
    print("\n ")
    message_content = ""
    while message_content != "exit":
        message_content = input("Your message: ")
        if message_content != "":
            message = username + ": " + message_content
            send(message)
        else:
            print("Message can't be empty.")


def configure_distribute():
    global s
    host = input("Server IP Address: ")
    port = input("Server Port: ")
    s.connect((host, int(port)))


def send(message):
    s.send(message.encode())
