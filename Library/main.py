
from table import *
from Connection import *

if __name__ == "__main__":
    server = Connection("localhost", "username", "password")
    
    # table = server.get("tabletest")
    able = server.get("tabletest")
    # able.set("isaac", [1, 2, 3])
    # able.set("kenzie", [4, 5, 6])
    # able.set("carson", [7, 8, 9])
    # able.set("feranmi", [10, 11, 12])
    
    isaac = able.get("isaac")
    print('table:',isaac)
    server.closeRemote()
    exit()