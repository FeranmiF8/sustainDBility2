
from socket import *
import pandas as pd
import os

# data = {
#     "Temperature":[12, 43, 35],
#     "Moisture":[65, 43, 32]
# }

# df = pd.DataFrame(data)

# df.to_csv("test.csv")

# print(df)

datajson = {
    "method":"set",
    "username":"kenzie",
    "accountkey":"poop",
    "tableName":"table1",
    "key":["Isaac", "Ken"],
    "data":[['epic', 69, 420, 'Hus'], ['cool', 70, 421, 'fishdad', 'swe']]
}

print(datajson["method"])

# get func call
def getCall(username, key):
    fileList = os.listdir(f"./{username}_{key}")

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

if not os.path.isdir(f"./{datajson['username']}_{datajson['accountkey']}"):
    os.mkdir(f"./{datajson['username']}_{datajson['accountkey']}")

if datajson["method"] == "get":
    getCall()
elif datajson["method"] == "set":
    setCall(datajson["username"], datajson["accountkey"], datajson["tableName"], datajson["data"], datajson["key"])


tcpSerSock = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
tcpSerSock.bind(('localhost',serverPort))
tcpSerSock.listen(1)

# while 1:
#     # Start receiving data from the client
#     print('Ready to serve...')
#     tcpCliSock, addr = tcpSerSock.accept()
#     print('Received a connection from:', addr)
#     message = tcpCliSock.recv(4096).decode()
#     print(message)
    
#     tcpCliSock.close()
# # Fill in start.
# tcpSerSock.close()