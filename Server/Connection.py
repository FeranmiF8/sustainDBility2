import argparse
import socket
import threading
from time import sleep
import random
import table


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


    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password

    
    def connect(self, ip, user, password):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((ip, 10000))

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
        self.conn.sendall("get " + key)
        data = self.conn.recv(1024)
        return data

    def set(self, key, value):
        self.conn.sendall("set " + key + " " + value)
        data = self.conn.recv(1024)
        return data
    
    def delete(self, key):
        self.conn.sendall("delete " + key)
        data = self.conn.recv(1024)
        return data




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
