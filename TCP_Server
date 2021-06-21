
#!/usr/bin/env python3
# #python3 /home/estufaTabaco/main.py
#
# import time
# import threading #https://www.tutorialspoint.com/python3/python_multithreading.htm
# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit
# from flask_cors import CORS
# import time
#
# app = Flask(__name__)
# #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# CORS(app)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, cors_allowed_origins='*')
#
# @app.route('/')
# def index():
#     print('conectado')
#
# @socketio.on('my event')
# def handle_my_custom_event(data):
#     emit('my response', {'data': message['data']}, broadcast=True)
#
# @socketio.on('my broadcast event')
# def test_message(message):
#     # emit('my response', {'data': message['data']}, broadcast=True)
#     emit('my event', {'data': message}, broadcast=True)
#
# @socketio.on('connect')
# def test_connect():
#     print('conectando connect')
#     try:
#         emit('my response', {'data': 'Connected22'})
#         emit('my event', {'data': 'Connected22'}, broadcast=True)
#     except Exception as error:
#         print('erro:', error)
#
# # @socketio.on('')
# # def test():
# #     print('conectando connect')
# #     emit('my response', {'data': 'Connected'})
#
# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       enviando()
#       print ("Exiting " + self.name)
#
# def enviando():
#     while True:
#         print('enviando')
#         time.sleep(4.0)
#         test_connect()
#
# if __name__ == '__main__':
#     thread = myThread(1, "Thread-1", 1)
#     thread.start()
#     print(11111)
# try:
#     socketio.run(app, port=5000)
# except Exception as e:
#     print("\n Execption occurs while starting the socketio server", str(e))
#     socketio.run(app, host='0.0.0.0', port=35494)
#     print(222222222)



import time
import threading #https://www.tutorialspoint.com/python3/python_multithreading.htm
import eventlet
import socketio #https://python-socketio.readthedocs.io/en/latest/server.html
global sio
sio = socketio.Server(cors_allowed_origins="*")
# app = socketio.WSGIApp(sio, static_files={
#     '/': {'content_type': 'text/html', 'filename': 'index.html'}
# })
app = socketio.WSGIApp(sio)

global vr
vr = 22

@sio.event
def connect(sid, environ):
    print('connect ok ', sid)
    sio.emit('my event', {'data': 'foobar'})
    teste()

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def teste():
    global vr
    print('Enviando mensagem ', vr)
    thread = myThread(1, "Thread-1", 1)
    thread.start()
    sio.emit('my event', {'data': 'mensagem teste'})
    sio.emit('message', {'data': 'mensagem teste'})

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      enviando()
      print ("Exiting " + self.name)

def enviando():
    global vr
    global sio
    while True:
        print('enviando', vr)
        time.sleep(6.0)
        sio.emit('my event', {'data': 'mensagem teste'})
        sio.emit('message', {'data': 'mensagem teste'})





if __name__ == '__main__':
    print(11111)
    eventlet.wsgi.server(eventlet.listen(('', 35494)), app)





# import socket
# import threading #https://www.tutorialspoint.com/python3/python_multithreading.htm
# import time
#
# # Create a server socket
# serverSocket = socket.socket()
# print("Server socket created")
# # Associate the server socket with the IP and Port
#
# ip = ""
# port = 35494
# serverSocket.bind((ip, port))
# print("Server socket bound with with ip {} port {}".format(ip, port))
# # Make the server listen for incoming connections
# serverSocket.listen()
# # Server incoming connections "one by one"
# count = 0
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       enviando()
#       print ("Exiting " + self.name)
#
# global address
# address = [('', 21000)]
# global conns
# conns = []
#
#
# def enviando():
#     print ('Conectado por', 'enviando apra clientes')
#     msgFromServer = "Hello UDP Client"
#     bytesToSend = str.encode(msgFromServer)
#     while True:
#         global conns
#         print('while enviando', conns, bytesToSend)
#         #UDPServerSocket.sendto(bytesToSend, ('<broadcast>', 20001))
#         #for addres in address:
#         for i in range(len(conns)):
#             try:
#                 print(len(conns), 'indice:', i)
#                 conns[i].send(bytesToSend)
#             except Exception as error:
#                 print('Desconectado Cliente: ', len(conns))
#                 del conns[i]
#                 break
#         time.sleep(4.0)
#
#
# thread = myThread(1, "Thread-1", 1)
# thread.start()
#
# while (True):
#     (clientConnection, clientAddress) = serverSocket.accept()
#     count = count + 1
#     print('clientAddress', clientAddress)
#     print('clientConnection', clientConnection)
#     conns.append(clientConnection)
#     print("Accepted {} connections so far".format(count))
#     # read from client connection
#     msg1 = "Conectado com o Server 1"
#     msg1Bytes = str.encode(msg1)
#     clientConnection.send(msg1Bytes)
#





#server UDP TESTADO
# import socket
# import threading #https://www.tutorialspoint.com/python3/python_multithreading.htm
# import time
#
# localIP = ""
# localPort = 20001
# bufferSize = 1024
# msgFromServer = "Hello UDP Client"
# bytesToSend = str.encode(msgFromServer)
#
# # Create a datagram socket
#
# UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#
# # Bind to address and ip
# UDPServerSocket.bind((localIP, localPort))
# print("UDP server up and listening")
# # Listen for incoming datagrams
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       enviando()
#       print ("Exiting " + self.name)
#
# global address
# address = [('', 21000)]
#
# def enviando():
#     print ('Conectado por', 'enviando apra clientes')
#
#     while True:
#         global address
#         print('while enviando', address, bytesToSend)
#         #UDPServerSocket.sendto(bytesToSend, ('<broadcast>', 20001))
#         #for addres in address:
#         for i in range(len(address)):
#             print(address[i])
#             UDPServerSocket.sendto(bytesToSend, address[i])
#         time.sleep(4.0)
#
#
# thread = myThread(1, "Thread-1", 1)
# thread.start()
#
# while (True):
#     bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
#     message = bytesAddressPair[0]
#     address.append(bytesAddressPair[1])
#     clientMsg = "Message from Client:{}".format(message)
#     clientIP = "Client IP Address:{}".format(address)
#
#     print(clientMsg)
#     print(clientIP)
#
#     # Sending a reply to client
#     UDPServerSocket.sendto(bytesToSend, bytesAddressPair[1])








#
# import socket
# import time
# import json
#
# HOST = '192.168.0.100'
# PORT = 5004
# ADDR = (HOST, PORT)
#
# #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #s.connect(ADDR)
#
# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
# client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
# # Enable broadcasting mode
# client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# client.bind(("", 37020))
#
# HOST = socket.gethostbyname(socket.gethostname()) #PEGANDO O MEU IP
# print(HOST)
# while True:
#     print('loop')
#     m = json.dumps({"id": 2, "name": "abc"})
#     client.sendto(bytes(m,encoding="utf-8"), ('<broadcast>', 37020))
#     time.sleep(4)

    #data, addr = client.recvfrom(1024)


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
