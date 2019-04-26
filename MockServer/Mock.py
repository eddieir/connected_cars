#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import socket
import sys
import time
import threading
from _thread import *
import json
print_lock = threading.Lock()
file_name = sys.argv[1]
host = "192.168.222.31"
port = 1235
buf = 2048
datastore = []
def ReadData():
    #file_name = input('Please enter your file name: ')
    
    
    data = open(file_name,'r')
    lines = data.readlines()
    Mlines = str(lines).split()
    #print(Mlines[0:50])
    data.close()
    return Mlines

#thread function    
def threaded(c):
    while True:
        #data receive from the client
        data = c.recv(1024**2)
        if not data:
            print("BYEEEEEEEEEEEEEEEE")
            print_lock.release()
            break
        data = data[::-1]
        c.send(data)
        time.sleep(2)
    c.close()    


def Main():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
    s.listen(5)
    print("Socket binded to port", port)
    data = open(file_name,'r')
    lines = data.readlines()
    mylist = lines[0].split('�')
    # json output
    with open('data1.json','w') as  outfile:
        json.dump(mylist,outfile) 
    for line in lines:
        datastore.append(line.strip().strip())
        #dataJson = json.loads(str(datastore))
    Mlines = str(lines).split()
    #print(Mlines[0:50])
    data.close()

    with open('data1.json','r') as json_file:
        Sending_info = json.load(json_file)
    #data = ReadData()
    while True:
        c,addr = s.accept()
        c.sendto((str(Sending_info)).encode(), (host, port))
        #print (lines)
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1]) 
        print(Sending_info[0])
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,))
    c.close()    

"""
def Stream():
    # Lets's initial the IP and port of the UDP server
    ip_address = "127.0.0.1"
    port = 1234
    buf = 2048
    connection  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #data = ReadData()
    connection.sendto((file_name).encode(), (ip_address, port))
    #connection.sendto(int("Data"), (ip_address, port))
    print("Sending file"  + file_name)
    data = ReadData()
    while(data):
        if(connection.sendto((file_name).encode(), (ip_address, port))):
            Ndata = data
            #time.sleep(0.02) 
    return ip_address,port,buf,connection

"""

if __name__ == "__main__":
    print("IP address is:", host)
    print("port address is:", port)
    print("buffer size is:", buf)
    Main()
    """ReadData()
    dataStream = Stream()
    print("IP address is:", dataStream[0])
    print("port address is:", dataStream[1])
    print("buffer size is:", dataStream[2])
    threaded()"""
    #print(dataStream.ip_address)
    #print(dataStream.port)
    #print(dataStream.buf)
