import pickle
from dotenv import load_dotenv
import socket
import os
load_dotenv()


sock = socket.socket()
sock.connect((os.getenv('HOST'), int(os.getenv('PORT'))))


p, g, a = 7, 5, 3
# генерируем ключ диффи-хелфмана
A = g ** a % p
# отправляем на сервер
sock.send(pickle.dumps((p, g, A)))
# получаем от сервера B
msg = sock.recv(1024)
B = pickle.loads(msg)
# проверяем правильность генерации пары ключей
K = B ** a % p
print("K =", K)

# вводим сообщение
message = input()
# конвертируем каждый символ сообщения в его байтовое представление
bits = list(map(ord, list(message)))
# к каждому байту прибавляем смещение K
bits = [i+K for i in bits]

# склеиваем символы по пробелу и передаём на сервер
message = ' '.join(list(map(str, bits)))
sock.send(message.encode())

sock.close()
