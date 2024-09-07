import socket

s = socket.socket()

host = "localhost"
port = 4000
s.connect((host, port))

fileName = input("Enter a file name: ")    
s.send(fileName.encode())

content = s.recv(1024)
print(content.decode())

s.close()