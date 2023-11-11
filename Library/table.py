

class Table:
    name = ""
    data = []
    server = None
    
    '''
    constructor for table object, is only used by the 'Connection' class
    @param name: name of table
    @param data: data of table
    @param server: server object
    '''
    def __init__(self, name, data, server):
        self.name = name
        self.data = data
        self.server = server
        print('table object created')
        
    '''
    gets value from the data that matches the key
    @param key: key to search for
    returns: value of key
    '''
    def get(self, key):
        # print(self.data)
        for i in self.data:
            print(i)
            if i[0] == key:
                print('value',i[1])
                return i[1]
        print('Data not found')
    
    
    '''
    Adds a value to the table and sends it to the server
    @param key: key to add
    @param value: data to add
    '''
    def set(self, key, value):
        print(key, value)
        self.data.append([key, value])
        self.server.setTable(self)
    
    '''
    deletes a value from the table and sends it to the server
    @param key: key to delete
    '''
    def delete(self, key):
        for i in self.data:
            if i[0] == key:
                self.data.remove(i)
                break
        self.server.setTable(self)
        
    def test(self):
        print('object works')
        
        
        