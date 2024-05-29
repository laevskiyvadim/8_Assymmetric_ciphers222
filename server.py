import pickle
from dotenv import load_dotenv
import socket
import os
load_dotenv()

sock = socket.socket()
sock.bind((os.getenv('HOST'), int(os.getenv('PORT'))))
sock.listen(1)
conn, addr = sock.accept()

# получаем от клиента ключ и свободные числа
msg = conn.recv(1024)
b = 9
p, g, A = pickle.loads(msg)
# генерируем B и отправляем на клиента
B = g ** b % p
conn.send(pickle.dumps(B))
K = A ** b % p
print("K =", K)

# получаем от клиента защифрованное сообщение
message = conn.recv(1024)

message = message.decode()
# разделяем сообщение по пробелу и конвертируем каждый символ в число
message = list(map(int, message.split()))
# делаем обратное смещение кода символа
message = [i-K for i in message]
# преобразуем кодовые представления символов в символы
message = ''.join(list(map(chr, message)))

print(message)

conn.close()
