import socket

host = "localhost"
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

print("Server listening on port", port)
s.listen(1)

connection, address = s.accept()

fileName = connection.recv(1024)
try:
    f = open(fileName, "rb")
    content = f.read()
    connection.send(content)
    f.close()
except FileNotFoundError:
    print("File does not exists")
    connection.send(b"File does not exist")
    
connection.close()