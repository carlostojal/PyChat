# PyChat
Python chat based in sockets.

## How it works?
PyChat uses Python sockets to send data between users.
It uses bus network typology.
To send a message, the message will go through all users to the server, and then the server will resend it to the 1st client, then the 1st client sends to the 2nd, etc.
Message will only be shown when it comes from the server.


## How to use
* Run server.py on the server
* Run send_client.py on the first client, using the server IP address and port.
* The same for client_receive.py.
    * Here, it will ask you to configure the distributor. The distributor is responsible to send your message to the client connected to you.
    * It will ask if will another user connect with you, this means if you are the last user to connect or not.
* The second client must do the same, but using the first client IP and port, as the third must use the second's, etc.
