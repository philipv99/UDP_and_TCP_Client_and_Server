from socket import *
import json
import threading

Log = [
   {"id":1, "ppm": 100},
   {"id":2, "ppm": 232},
   {"id":3, "ppm": 343}
   ]

def handleClient(cennectionSocket, addr):
   print(str(addr) + "has connected")
   while True:
      ClientLog = cennectionSocket.recv(1024).decode()
      try:
         jsonLog = json.loads(ClientLog)
      except:
         print("message not json")

      print(jsonLog)
      Log.append(jsonLog)
      jsonsend = json.dumps(Log)
      print(Log)
      cennectionSocket.send(jsonsend.encode())



serverPort = 30303
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('server is ready to listen')

while True:
   cennectionSocket, addr = serverSocket.accept()
   threading.Thread(target=handleClient, args=(cennectionSocket, addr)).start()

# while True:
#    ClientLog = cennectionSocket.recv(1024).decode()
#    NewLog = json.loads(ClientLog)
#    print(str(ClientLog))