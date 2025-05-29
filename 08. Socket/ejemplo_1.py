import socket
import ssl

HOST = "www.py4e.com"       # Solo el dominio, sin la ruta
PORT = 443                  # Puerto HTTPS

# Crear socket y envoltura SSL usando with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
    
    # Conectar al HOST y puerto HTTPS (443)
    mysock.connect((HOST, PORT))

    # Crear contexto SSL
    context = ssl.create_default_context()
    
    # Envolver el socket en SSL (debido al uso de HTTPS)
    with context.wrap_socket(mysock, server_hostname=HOST) as ssl_sock:

        # Enviar solicitud HTTP
        request = (
            "GET /code3/romeo.txt HTTP/1.1\r\n"    # ruta del recurso
            "Host: www.py4e.com\r\n"               # host del servidor 
            "Connection: close\r\n"                # cerrar conexión después de la respuesta   
            "\r\n"
        )
        ssl_sock.send(request.encode())

        # Recibir datos
        while True:
            data = ssl_sock.recv(512)
            if not data:
                break
            print(data.decode(), end='')
