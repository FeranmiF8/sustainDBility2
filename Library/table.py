

class table:
    name = ""
    data = []
    server = None
    
    def __init__(self, name, server):
        self.name = name
        self.data = []
        data = server.getTable(name)
        
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
        
        
        