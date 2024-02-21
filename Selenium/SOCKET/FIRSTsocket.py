import socket

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.connect(('www.w3.org', 80))
Read = 'GET https:www.w3.org/Summary.txt HTTP/1.0\r\nHost: www.w3.org\r\n\r\n'.encode()
Server.send(Read)

while True:
    info = Server.recv(512)
    if len(info) < 1:
        break
    print(info.decode(), end='')

Server.close()
