#!/usr/bin/env python

import socket

host = socket.gethostbyname(socket.getfqdn())
port = 7000
backlog = 5
size = 1024

print "Server hostname: ", host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        client.send(data)
    client.close()
