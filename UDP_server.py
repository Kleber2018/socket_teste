
#!/usr/bin/env python3

##https://pythontic.com/modules/socket/client-server-example
# #python3 /home/estufaTabaco/main.py

import socket
import threading #https://www.tutorialspoint.com/python3/python_multithreading.htm
import time

localIP = ""
localPort = 20001
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams

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

global address
address = [('', 21000)]

def enviando(): #corre a lista de clientes para enviar mensagem apra eles periodicamente
    print ('Conectado por', 'enviando apra clientes')

    while True:
        global address
        print('while enviando', address, bytesToSend)
        #UDPServerSocket.sendto(bytesToSend, ('<broadcast>', 20001))
        #for addres in address:
        for i in range(len(address)):
            print(address[i])
            UDPServerSocket.sendto(bytesToSend, address[i])
        time.sleep(4.0)


thread = myThread(1, "Thread-1", 1) #thread para enviar as mensagens para os clientes em segundo plano
thread.start()

while (True): #while que trata as novas conecções
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address.append(bytesAddressPair[1])
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, bytesAddressPair[1])
