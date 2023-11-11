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
    buffer_S = ""
    lock = threading.Lock()
    collect_thread = None
    stop = None
    socket_timeout = 0.1
    reorder_msg_S = None
    tables = []


    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password

    
    def connect(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.ip, 10000))

        # start the thread to receive data on the connection
        # self.collect_thread = threading.Thread(name="Collector", target=self.collect)
        # self.stop = False
        # self.collect_thread.start()

    def disconnect(self):
        if self.collect_thread:
            self.stop = True
            # self.collect_thread.join()

    def __del__(self):
        if self.sock is not None:
            self.sock.close()
        if self.conn is not None:
            self.conn.close()

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




# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Network layer implementation.")
#     parser.add_argument(
#         "role",
#         help="Role is either sender or receiver.",
#         choices=["sender", "receiver"],
#     )
#     parser.add_argument("receiver", help="receiver.")
#     parser.add_argument("port", help="Port.", type=int)
#     args = parser.parse_args()

#     network = NetworkLayer(args.role, args.receiver, args.port)
#     if args.role == "sender":
#         network.udt_send("MSG_FROM_SENDER")
#         sleep(2)
#         print(network.udt_receive())
#         network.disconnect()

#     else:
#         sleep(1)
#         print(network.udt_receive())
#         network.udt_send("MSG_FROM_RECEIVER")
#         network.disconnect()
