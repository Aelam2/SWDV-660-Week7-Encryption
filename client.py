import socket    
import random 

#simple cipher using length of public key and mod 17
def encryptWithPublicKey(publicKey, sessionCipher):
    cipherText = []
    for cipherChar in sessionCipher:
        newLetter = (ord(cipherChar) - len(publicKey) % 17) 
        cipherText.append(chr(newLetter))

    return ''.join(cipherText)

serverName = ''
publicKey = ''
sessionCipher = 'session cipher key'

# Connet to Elam Test Server to request serverName
s = socket.socket()                        
s.connect(('localhost', 9500)) 
req = s.send('Name Request') # Request the name of the server
serverName = s.recv(1024)
print('Requested Server Name: ' + serverName)
s.close()  # close connection with the Server 

# connect to localhost port Certificate Authority
# and request public key for Elam Test Server 
s = socket.socket()                        
s.connect(('localhost', 9000)) 
req = s.send(serverName) #Server Name from first request
publicKey = s.recv(1024)
print('Public Key returned by CA: ' + publicKey)
s.close()  # close connection with CA Server 

# Reconnect to the Elam Test Server with encrypted cipher key
encryptedKey = encryptWithPublicKey(publicKey, sessionCipher)
print('Encrptyed Session Key: ' + encryptedKey) 

s = socket.socket()                        
s.connect(('localhost', 9500)) 
req = s.send(encryptedKey) # Send message encrypyted by public key
cipherAcknowledgement = s.recv(1024)
print('Returned ciphered message: ' + cipherAcknowledgement)
s.close()  # close connection with the Server 

if(cipherAcknowledgement == encryptWithPublicKey(publicKey, 'session cipher key acknowledgement')):
    print('Begin transferring data')


