from socket import *
import json

serverName = "localhost"
serverPort = 30303
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

Log = []
data = {"id": 0, "ppm": 0}

data["id"] = input("skriv id \n")
data["ppm"] = input("skirv ppm \n")

print(data)
jsonData = json.dumps(data)
clientSocket.send(jsonData.encode())
newLog = clientSocket.recv(1024).decode()
Log = json.loads(newLog)
print(Log)


