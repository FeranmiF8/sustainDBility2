
from table import *
from Connection import *

if __name__ == "__main__":
    server = Connection("10.13.155.107", "username", "password")
    
    table = server.get("tabletest")
    table.set("isaac", [1, 2, 3])
    table.set("kenzie", [4, 5, 6])
    table.set("carson", [7, 8, 9])
    table.set("feranmi", [10, 11, 12])
    
    isaac = table.get("isaac")
    print(isaac)
    exit()