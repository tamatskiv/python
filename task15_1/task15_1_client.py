#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 9090))

while True:
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    a = input()
    sock.send(a.encode('utf-8'))

sock.close()
