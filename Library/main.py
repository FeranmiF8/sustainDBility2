
from table import *
from Connection import *



def addDataTest(table):
    table.set("jump", [5, 8, 10, 12])
    table.set("whisper", [3, 7, 9])
    table.set("dance", [2, 4, 6, 8, 10])
    table.set("explore", [1, 3, 5, 7])
    table.set("create", [4, 6, 9, 11])
    table.set("laugh", [2, 5, 8])
    table.set("discover", [1, 3, 6, 9, 12])
    table.set("run", [4, 7, 10])
    table.set("sing", [3, 6, 9, 12])
    table.set("dream", [2, 5, 8, 11])
    table.set("paint", [3, 6, 9])
    table.set("climb", [2, 5, 8, 11])
    table.set("whirl", [4, 7, 10, 13])
    table.set("meditate", [1, 4, 7, 10, 13])
    table.set("navigate", [3, 6, 9, 12])
    table.set("compose", [2, 5, 8])
    table.set("rejoice", [4, 7, 10])
    table.set("shimmer", [1, 3, 5, 7, 9])
    table.set("journey", [2, 4, 6, 8, 10])
    table.set("sparkle", [5, 8, 11])
    
def getDataTest(table):
    print('run data: ', table.get("run"))
    print('rejoice data: ', table.get("rejoice"))
    print('meditate first value: ', table.get("meditate")[0])
    

if __name__ == "__main__":
    con = Connection("localhost", "username", "password")
    
    table = con.getTable("tabletest")
    # addDataTest(table)
    # getDataTest(table)
    con.closeRemote()
    exit()