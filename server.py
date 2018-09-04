#!/bin/env python3
# encoding: utf-8

import socket
import sys

ip = '0.0.0.0'
porta = 1234

sock = socket.socket()
sock.bind((ip, porta))
print('Listening to %s:%s' % (ip, porta))
sock.listen(10)
conn, addr = sock.accept()
print('Connected to %s:%s' % (addr[0], addr[1]))

while True:
    cmd = input("cmd > ")
    if len(cmd) > 0:
        conn.send(cmd.encode(errors='ignore'))
        data = conn.recv(102400).decode(errors='ignore')
        print(data)
    if cmd == 'q':
        conn.close()
        sys.exit()
    else:
        continue
