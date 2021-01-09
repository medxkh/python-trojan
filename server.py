import socket 

HOST = 
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

client , address = server.accept()

while True:
    print(f"connect to {address}")
    cmd_input = input('Enter command please')
    client.send(cmd_input.encode('utf_8'))
    print(client.recv(1024).decode('utf_8'))