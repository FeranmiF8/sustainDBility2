
from socket import *
import pandas as pd
import os
import json
import csv

# datajson = {
#     "method":"set",
#     "username":"kenzie",
#     "accountkey":"poop",
#     "tableName":"table1",
#     "data":{
#         "keys":['isaac', 'kenzie', 'carson','feranmi'],
#         "data":[[65, 43, 32],[65, 43, 32],[65, 43, 32],[65, 43, 32]]
#     }
# }

# print(datajson["method"])

# get func call
def getCall(username, key):
    fileList = os.listdir(f"./{username}_{key}")
    print('table found:',fileList)
    try:
        #file = open(f"./{username}_{key}/{fileList[0]}", "r")
        
        ret = []
        csv_reader = None
        with open(f"./{username}_{key}/{fileList[0]}", 'r') as file:
            print('file found')
            csv_reader = csv.reader(file)
            for row in csv_reader:
            # Each row is a list representing the columns in that row
                row.pop(0)
                ret.append(row)
            file.close()
        
        ret.pop(0)
        print(ret)
        return ret
    except Exception as e:
        print(e)
        print('file not found')
        return

# set func call
def setCall(username, accountkey, table, data, key):

    df = pd.DataFrame({
        "key":[],
        "data":[]
    }, dtype=object)
    for i in range(len(key)):
        df.loc[i] = [key[i], data[i]]

    df.to_csv(f"./{username}_{accountkey}/{table}.csv")

# delete func call
def deleteCall():
    return

tcpSerSock = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
tcpSerSock.bind(('localhost',serverPort))
tcpSerSock.listen(1)

while 1:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(4096).decode()
    # print('message: ',message)
    if message == '':
        continue
    data = json.loads(message)
    if data["method"] == "get":
        getCall(data["username"],data["accountkey"])
    elif data["method"] == "set":
        setCall(data["username"], data["accountkey"], data["tableName"], data["data"]["data"], data["data"]["key"])
    elif data["method"] == "quit":
        break
    tcpCliSock.close()
tcpSerSock.close()
