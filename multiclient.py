# Python program to implement client side of chat room.
import socket
import select
import sys
import os
import subprocess
import pyfiglet
from termcolor import cprint

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = "0.tcp.in.ngrok.io"
Port = sys.argv[1]
server.connect((IP_address, Port))
name = os.popen('echo "$USER"')

while True:
    try:
        sockets_list = [sys.stdin, server]
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
        for socks in read_sockets:
                if socks == server:
                        message = socks.recv(2048)
                        if OSError:
                            pass
                        print(message)
                else:
                    message = sys.stdin.readline() 
                    server.send(message.encode()), sys.stdout.write("<You>"), sys.stdout.write(message), sys.stdout.flush()
    except KeyboardInterrupt:
        print("Connection has been closed")
        exit(1)
server.close()
