import socket
import sys

port = 9000
s = socket.socket()

s.bind(('', port)) 
s.listen(5)

# List of registered servers and there public keys
servers = [
    {'serverName': 'Elam Test Server', 'publicKey': 'My Server Public Key'}
]

while True:
    conn, addr = s.accept()
    clientData = conn.recv(1024).decode()

    reply = ''

    #Loop through registered servers and see if any match clients requested server
    for server in servers:
        if(clientData.lower() == server['serverName'].lower()):
            reply = server['publicKey']
            break
        else:
            reply = 'Requested server not found.'

    conn.send(reply.encode())
    conn.close()