import socket

HOST = "data.pr4e.org"       # Solo el dominio, sin la ruta
PORT = 80                  # Puerto HTTP

# Crear socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:

    # Conectar al HOST y puerto HTTP (80)
    mysock.connect((HOST, PORT))

    # Enviar solicitud HTTP
    request = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(request)
    
    # Recibir datos
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
