
from socket import *
import pandas as pd
import os
import json

# data = {
#     "Temperature":[12, 43, 35],
#     "Moisture":[65, 43, 32]
# }

# df = pd.DataFrame(data)

# df.to_csv("test.csv")

# print(df)

# print(datajson["method"])

# get func call
def getCall(username, key, socket):
    fileList = os.listdir(f"./{username}_{key}")
    
    returnStr = ""
    json_data = {}
    for fileName in fileList:
        data = pd.read_csv(f"./{username}_{key}/{fileName}")
        # keys_col = data[["keys"]].to_string(index=False)
        # data_col = data[["data"]].to_string(index=False)
        # returnStr += keys_col + data_col
        json_data[f"{fileName}"] = data.to_json(orient='records', lines=True)
        # json_data += data.to_json(orient='records', lines=True)
    # print(json_data)
    print('sent data to remote client')
    socket.sendall(json.dumps(json_data).encode())
    # print(returnStr.replace("\n", " "))

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
    message = tcpCliSock.recv(4096).decode()
    # print('message: ',message)
    if message == '':
        continue
    data = json.loads(message)
    if data["method"] == "get":
        getCall(data["username"],data["accountkey"], tcpCliSock)
    elif data["method"] == "set":
        setCall(data["username"], data["accountkey"], data["tableName"], data["data"]["data"], data["data"]["key"])
    elif data["method"] == "quit":
        tcpCliSock.close()
        break
    tcpCliSock.close()
tcpSerSock.close()
