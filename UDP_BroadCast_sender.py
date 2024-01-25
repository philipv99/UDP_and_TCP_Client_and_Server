import random
import time
import socket
import json


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def makeMassege(): # laver beskeden
   data = {"id": random.randint(1,45), "ppm": random.randint(350, 1400)}
   return json.dumps(data)

while True: # sender besked og venter
   massege = makeMassege()
   client.sendto(massege.encode(), ('<broadcast>', 30303)) # bradcaster en besked på port 14014
   print("Send: (" + massege + ")")
   time.sleep(random.randint(2,5))