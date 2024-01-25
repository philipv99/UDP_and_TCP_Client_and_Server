import socket
from socket import *
import json

Log = []

BroadCast = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
BroadCast.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
BroadCast.bind(("", 30303)) # setter servern til at lytte på port 14014


serverName = "localhost"
serverPort = 30303
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

print("resiver ready")

while True:
   dataReseved, addr = BroadCast.recvfrom(1024)
   data = dataReseved.decode()
   print("received message: " + data)
   jsonMessage = json.loads(data) 
   Log.append(jsonMessage)
   JLog = json.dumps(Log)
   clientSocket.send(JLog.encode())
