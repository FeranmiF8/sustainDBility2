import argparse
import socket
import threading
from time import sleep
import random
import table
import json


## Provides an abstraction for the network layer
class Connection:

    # class variables
    sock = None
    conn = None
    ip = ''
    user = ''
    password = ''


    '''
    constructor for Connection object
    @param ip: IP address of the server
    @param user: username for authentication
    @param password: password for authentication
    '''
    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password

    
    '''
    Connect to the server
    '''
    def connect(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.ip, 10000))

        # start the thread to receive data on the connection
        # self.collect_thread = threading.Thread(name="Collector", target=self.collect)
        # self.stop = False
        # self.collect_thread.start()

    '''
    Disconnect from the server
    '''
    def disconnect(self):
        if self.collect_thread:
            self.stop = True
            # self.collect_thread.join()

    '''
    Destructor for Connection object
    '''
    def __del__(self):
        if self.sock is not None:
            self.sock.close()
        if self.conn is not None:
            self.conn.close()

    '''
    Get table data from the server
    @param key: name of the table
    @return: table object
    '''
    def get(self, key):
        self.connect()
        for i in self.tables:
            if i.name == key:
                return i
        json_obj = {
            "method": "get",
            "username": self.user,
            "accountkey": self.password,
            "tableName": key,
            "data": ""
        }

        req = json.dumps(json_obj)
        self.conn.sendall(req.encode())
        data = self.conn.recv(1024)
        newTable = table(key, data, self)
        self.tables.append(newTable)
        self.__del__()
        return  newTable


    '''
    Set table data to the server
    @param table: table object
    '''
    def setTable(self, table):
        for i in self.tables:
            if i.name == table.name:
                i = table
                break
        if table not in self.tables:
            self.tables.append(table)
        self.connect()
        json_obj = {
            "method": "set",
            "username": self.user,
            "accountkey": self.password,
            "tableName": table.name,
            "data": table.data
        }

        req = json.dumps(json_obj)
        self.conn.sendall(req.encode())
        self.__del__()


