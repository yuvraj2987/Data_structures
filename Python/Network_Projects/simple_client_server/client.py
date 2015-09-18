#!/usr/bin/env python

import socket

host = '54.164.153.189'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#remote_ip = s.gethostbyname(host)
#print "IP address of ",host, " is ", remote_ip
s.connect((host, port))
print "Connected to the host"
s.send('Hello, World')
print "Send data to host"
data = s.recv(size)
s.close()
print "Received Data: ", data
