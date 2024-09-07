import socket

host = "localhost"
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

print("Server listening on port", port)
s.listen(1)

connection, address = s.accept()

print("Connection from:", str(address))

connection.send(b"Hello, how are you?")
connection.send("Bye".encode())
connection.close()