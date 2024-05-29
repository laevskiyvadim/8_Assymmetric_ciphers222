import pickle
from dotenv import load_dotenv
import socket
import os
from helpers import power
load_dotenv()


sock = socket.socket()
sock.connect((os.getenv('HOST'), int(os.getenv('PORT'))))

p, g, a = 7, 5, 3
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))
msg = sock.recv(1024)
B = pickle.loads(msg)
K = B ** a % p
print("K =", K)

message = input()
bits = list(map(ord, list(message)))
bits = [i+K for i in bits]

message = ' '.join(list(map(str, bits)))
sock.send(message.encode())

sock.close()
