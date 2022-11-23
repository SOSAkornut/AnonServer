import socket
import select
import sys
from _thread import *
import pyfiglet
from termcolor import cprint

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

cprint(pyfiglet.figlet_format("ANON_SERVER"), "green")
cprint(pyfiglet.figlet_format("made by SOSAkornut", font="digital"), "cyan")
print("\n")
cprint("waiting for incoming connections", "yellow")


IP_address = "localhost"
Port =  9999
server.bind((IP_address, Port))
server.listen(100)
conn, addr = server.accept()
list_of_clients = []
close = 1

def clientthread(conn, addr):
    conn.send(b"Welcome to this chatroom!")
    while True:

        #try:
            message = conn.recv(2048)

            if message:
                    #print(("<" + addr[0] + "> " + message.decode()))
                    print(f"<{addr[0]}> {message.decode()} ")
                    message_to_send = "<" + addr[0] + "> " + message.decode()
                    broadcast(message_to_send, conn)
            else:
                try:
                    if close == 1:
                        cprint(" a client has left", "red")
                        close = 0
                    else:
                        close = 1
                except UnboundLocalError:
                    pass
                remove(conn)

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                message = message.encode()
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    cprint("A client has joined", "green")
    start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()
