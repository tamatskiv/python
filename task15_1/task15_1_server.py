#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
names = ('Vasya', 'Bogdan', 'Liuda', 'Masha')
phrases = ('How did you get here?',
           'How old are you?',
           'What do you think is strange?',
           'How many brothers/sisters do you have',
           'How are you?')
start = True
sock.connect(('', 9090))

sock.listen(1)
print('Waiting for connection...')

conn, addr = sock.accept()
print('Connection from {}'.format(addr))

while True:
    if start:
        conn.send('Hello! I\'m dummy bot and you?'.encode('utf-8'))
        start = False

    response = conn.recv(1024)
    print(response.decode('utf-8'))

    if response.decode('utf-8') in names:
        conn.send('Nice to meet you '.encode('utf-8')
                  + response + '\n'.encode('utf-8'))
        continue
    elif response.decode('utf-8') == "How are you?":
        conn.send('Perfect!\n'.encode('utf-8'))
        continue
    elif response.decode('utf-8') == "Goodbye":
        conn.send('Bye, have a nice day!\n'.encode('utf-8'))
        break
    else:
        conn.send(random.choice(phrases).encode('utf-8') \
                  + '\n'.encode('utf-8'))
        continue

conn.close()