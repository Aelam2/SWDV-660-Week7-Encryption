# SWDV-660-Week7-Encryption

- Client requests server name from Test Server
- Test Server response with server name


- Client uses server name to request public key from Certificate Authority
- CA responds with public key


- Client encrypts session key with public key from CA
- Test Server also encrypts using its public key and compares results

- If Successful, send an acknowledgement and begin data transfer
