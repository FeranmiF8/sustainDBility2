

class Table:
    name = ""
    data = []
    server = None
    
    def __init__(self, name, data, server):
        self.name = name
        self.data = data
        self.server = server
        print('table object created')
        
    def get(self, key):
        for i in self.data:
            if i[0] == key:
                return i[1]
    
    
    def set(self, key, value):
        for i in self.data:
            if i[0] == key:
                i[1] = value
                break
            else:
                self.data.append([key, value])
                break
        self.server.setTable(self.name, self.data)
    
    def delete(self, key):
        for i in self.data:
            if i[0] == key:
                self.data.remove(i)
                break
        self.server.setTable(self.name, self.data)
        
    def test(self):
        print('object works')
        
        
        