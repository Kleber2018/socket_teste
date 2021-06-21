# #!/usr/bin/env python3
# #python3 /home/estufaTabaco/main_cliente.py
#


import socketio
sio = socketio.Client()
@sio.event
def connect():
    print('connection established')
@sio.event
def message(data):
    print('message received with ', data)
    #sio.emit('my response', {'response': 'my response'})
@sio.event
def disconnect():
    print('disconnected from server')
sio.connect('http://192.168.0.100:35494')

sio.wait()

# # import the socket module
# import socket
#
# # Create a socket instance
# socketObject = socket.socket()
# # Using the socket connect to a server...in this case localhost
# socketObject.connect(("192.168.0.100", 35494))
# print("Connected to localhost")
# # Send a message to the web server to supply a page as given by Host param of GET request
# HTTPMessage = "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"
# bytes = str.encode(HTTPMessage)
# socketObject.sendall(bytes)
# # Receive the data
# while (True):
#     data = socketObject.recv(1024)
#     print(data)
# socketObject.close()
#





#udp cliente TESTE FUNCIONANDO
# import socket
#
# msgFromClient = "Hello UDP Server"
#
# bytesToSend = str.encode(msgFromClient)
#
# serverAddressPort = ("192.168.100.142", 20001)
#
# bufferSize = 1024
#
# # Create a UDP socket at client side
#
# UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#
# # Send to server using created UDP socket
#
# UDPClientSocket.sendto(bytesToSend, serverAddressPort)
# print('esperando')
# msgFromServer = UDPClientSocket.recvfrom(bufferSize)
#
# msg = "Message from Server {}".format(msgFromServer[0])
#
# print(msg)







# import socket
# import time
#
# HOST = '192.168.0.100'
# PORT = 5004
# ADDR = (HOST, PORT)
#
# #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #s.connect(ADDR)
# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
# client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
# # Enable broadcasting mode
# client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# try:
#     client.bind(("192.168.100.142", 20001))
# except:
#     print('erro')
#
# HOST = socket.gethostbyname(socket.gethostname()) #PEGANDO O MEU IP
# print(HOST)
# while True:
#     data, addr = client.recvfrom(1024)
#     print("received message: %s"%data.decode('utf-8'))

# def send(msg):
#     message = msg.encode('utf-8')
#     #msg_length = len(message)
#     #send_length = str(msg_length).encode('utf-8')
#     #send_length += b' ' * (64 - len(send_length))
#     #print(send_length)
#     #s.send(send_length)
#     s.send(message)
#     print(s.recv(128).decode('utf-8'))
#
# send('olá teste')
# time.sleep(10)
# send('olá testewww')
# while True: #escutando o servidor
#     print('qhile')
#     print(s.recv(128).decode('utf-8'))
# time.sleep(50)
#
#
#
# #send('FIM')
