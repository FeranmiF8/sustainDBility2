
from table import *
from Connection import *

if __name__ == "__main__":
    server = Connection("10.13.155.107", "username", "password")
    
    server.test('hello gamers')
    
    print('poop')
    exit()