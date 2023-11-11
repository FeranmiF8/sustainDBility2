
from socket import *
import pandas as pd

# # data = {
# #     "Temperature":[12, 43, 35],
# #     "Moisture":[65, 43, 32]
# # }

# # df = pd.DataFrame(data)

# # df.to_csv("test.csv")

# # print(df)

# datajson = {
#     "method":"set",
#     "username":"kenzie",
#     "accountkey":"poop",
#     "tableName":"table1",
#     "data":{
#         "Temperature":[18, 43, 35],
#         "Moisture":[65, 43, 32]
#     }
# }

# print(datajson["method"])

# # get func call
# def getCall():
#     return

# # set func call
# def setCall(username, key, table, data):
#     df = pd.DataFrame(data)
#     df.to_csv(f"./{username}_{key}/{table}.csv")

# # delete func call
# def deleteCall():
#     return

# if datajson["method"] == "get":
#     getCall()
# elif datajson["method"] == "set":
#     setCall(datajson["username"], datajson["accountkey"], datajson["tableName"], datajson["data"])


tcpSerSock = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
tcpSerSock.bind(('',serverPort))
tcpSerSock.listen(1)

while 1:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(4096).decode()
    print(message)
    
    tcpCliSock.close()
# Fill in start.
tcpSerSock.close()