from socket import *
clientsocket = socket(AF_INET, SOCK_STREAM)
try:
    clientsocket.connect(('localhost',8080))
    cmd = 'GET http://localhost/page10.htm HTTP/1.0\r\n\r\n'.encode()
    clientsocket.send(cmd)
    while True:
            data = clientsocket.recv(512)
            if len(data) < 1:
                 break
            print(data.decode(), end='')

    clientsocket.close()
except Exception as exc:
    print(exc)
