import pickle
from dotenv import load_dotenv
import socket
import os
from helpers import power
load_dotenv()

sock = socket.socket()
sock.bind((os.getenv('HOST'), int(os.getenv('PORT'))))
sock.listen(1)
conn, addr = sock.accept()

msg = conn.recv(1024)
b = 9
p, g, A = pickle.loads(msg)
B = g ** b % p
conn.send(pickle.dumps(B))
K = A ** b % p
print("K =", K)


message = conn.recv(1024)

message = message.decode()
message = list(map(int, message.split()))
message = [i-K for i in message]
message = ''.join(list(map(chr, message)))
print(message)

conn.close()
