#!/usr/bin/env python3

import sys
import socket
import selectors
import types
import datetime
import os
mySelector = selectors.DefaultSelector()

def filechecker(myfilename):
    #read input filechecker
    fin = open(myfilename, "rt")
    #read file contents to the string
    data = fin.read()
    # replace all occurences of the required string
    data = data.replace('\n\n', '\n')
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(myfilename, "wt")
    #overwrite the input file with resulting data
    fin.write(data)
    #close the file
    fin.close()

def accept_wrapper(sock):
    conn, addr = sock.accept()    #Should be ready to read
    print("==========\nAt", datetime.datetime.now(), "Accepted connection from", addr, "\n==========")
    print("\U0001f600" *5)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    mySelector.register(conn, events, data=data)


def service_connection(key,mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(20480)
        if recv_data:
            data.outb += recv_data
        else:
            print("==========\n AT ", datetime.datetime.now(), "Closed connection to", data.addr, "\n==========")
            mySelector.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            mySize= sys.getsizeof(data.outb)
            print(mySize, " bytes recieved from ", data.addr[0], " on port ", data.addr[1])
            # print(str(sys.getsizeof(data.outb)) + "Bytes Recieved")
            myfname = ''.join(data.addr[0]).encode()
            myfname = str(myfname)
            myfname += str(data.addr[1])
            myfname += '.xyz'
            f = open(myfname, "ab")
            f.write(((data.outb)))
            # f.write (''.join(repr(data.outb)))
            f.close()
            filechecker(myfname)
            # with open(myfname, 'ab') as writer:
            #       writer.write(data.outb)
            # print ("\tEchoing", repr(data.outb), "to", data.addr)
            sent = sock.send(data.outb)    # Should be ready to write
            data.outb = data.outb[sent:]




if len(sys.argv) !=3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print("Listening on", (host, port))
lsock.setblocking(False)
mySelector.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = mySelector.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection (key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    mySelector.close()





