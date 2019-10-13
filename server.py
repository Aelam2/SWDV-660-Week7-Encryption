import socket
import sys

#Used for encrypting messages with public key
#simple cipher using length of public key and mod 17
def encryptWithPublicKey(publicKey, sessionCipher):
    cipherText = []
    for cipherChar in sessionCipher:
        newLetter = (ord(cipherChar) - len(publicKey) % 17) 
        cipherText.append(chr(newLetter))

    print('Encrptyed Session Key ' + ''.join(cipherText)) 
    return ''.join(cipherText)

publicKey = 'My Server Public Key'

port = 9500
s = socket.socket()

s.bind(('', port)) 
s.listen(5)

while True:
    conn, addr = s.accept()
    data = conn.recv(1024).decode()

    message = ''
    if(data.lower() == 'name request'):
        message = 'Elam Test Server'
    
    elif(data == encryptWithPublicKey(publicKey, 'session cipher key')):
        message = encryptWithPublicKey(publicKey, 'session cipher key acknowledgement')

    elif(data.lower() == 'hello'):
        message = 'Hi'

    else:
        message = 'Goodbye'

    conn.send(message.encode())
    conn.close()